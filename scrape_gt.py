from bs4 import BeautifulSoup as bs
import requests
import os


# import webdriver
from selenium import webdriver

def get_gt_data_tum():

    link = "https://cvg.cit.tum.de/data/datasets/rgbd-dataset/download"
    link = "https://cvg.cit.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_xyz-groundtruth.txt"

    html = requests.get(link)
    soup = bs(html.content, 'html.parser')

    print(soup.prettify())

    hrefs = []

    website_base= "https://cvg.cit.tum.de"

    print(soup.find('a'))
    link = soup.find('a')
    while link is not None:
        href_link = link.get('href')
        if href_link is not None and "groundtruth.txt" in href_link:
            hrefs.append(website_base+href_link)
        link = link.find_next('a')



    return hrefs





def save_gt_data_tum(hrefs, root_path="results", dataset="tum"):

    driver = webdriver.Chrome()

    for href in hrefs:
        seuqence = href.split('/')[-1].split('-')[0]
        save_path = os.path.join(root_path, dataset, seuqence, "groundtruth.txt")

        print(href)
        if os.path.exists(save_path):
            print("File already exists")
            continue

        driver.get(href)
        response = driver.page_source

        # get body of the response
        soup = bs(response, 'html.parser')
        body = soup.find('body').text

        # response = requests.get(href)

        # body = response

        # #'https://cvg.cit.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_xyz-groundtruth.txt'

        
        if not os.path.exists(os.path.join(root_path, dataset, seuqence)):
            os.makedirs(os.path.join(root_path, dataset, seuqence))
        

        # body = str(html.content) #.decode('utf-8')

        with open(save_path, 'w') as f:
            f.write(body)

        # exit(0)


def get_gt_data_euroc():
    
        link = "https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets"
        html = requests.get(link)
        soup = bs(html.content, 'html.parser')
    
        # print(soup.prettify())
    
        hrefs = []
    
        # website_base= "https://projects.asl.ethz.ch/datasets/"
    
        print(soup.find('a'))
        link = soup.find('a')
        while link is not None:
            href_link = link.get('href')
            if href_link is not None and ".zip" in href_link:
                hrefs.append(href_link)
            link = link.find_next('a')
    
    
    
        return hrefs


def main_tum():
    # gt_data = get_gt_data()
    # print(gt_data)

    # with open("gt_data.txt", 'w') as f:
    #     for data in gt_data:
    #         f.write(data+'\n')

    gt_data = []
    with open("gt_data.txt", 'r') as f:
        for line in f:
            gt_data.append(line.strip())
    

    save_gt_data_tum(gt_data)



def download_url(url, save_path, chunk_size=128):
    
    # os.system("wget -O "+save_path+" "+url)

    os.system("axel -n 10 -o "+save_path+" "+url)

    os.system("unzip "+save_path+" -d "+save_path.split('.')[0])

    

    # r = requests.get(url, stream=True)


    # with open(save_path, 'wb') as fd:
    #     for chunk in r.iter_content(chunk_size=chunk_size):
    #         fd.write(chunk)



def save_gt_data_euroc(hrefs, root_path="results", dataset="euroc"):

    # driver = webdriver.Chrome()

    for href in hrefs:

        #http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_01_easy/MH_01_easy.zip

        # temp directory to download the zip file
        temp_dir = "temp_download"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        # download the zip file
        file_name = href.split('/')[-1]
        download_url(href, os.path.join(temp_dir, file_name))

        exit(0)


        seuqence = href.split('/')[-1].split('.')[0]
        save_path = os.path.join(root_path, dataset, seuqence, "data.csv")

        print(href)
        if os.path.exists(save_path):
            print("File already exists")
            continue
        
        # download the zip file
        driver.get(href)

 
        response = driver.page_source

        # get body of the response
        soup = bs(response, 'html.parser')
        body = soup.find('body').text

        # response = requests.get(href)

        # body = response

        # #'https://cvg.cit.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_xyz-groundtruth.txt'

        
        if not os.path.exists(os.path.join(root_path, dataset, seuqence)):
            os.makedirs(os.path.join(root_path, dataset, seuqence))
        

        # body = str(html.content) #.decode('utf-8')

        with open(save_path, 'w') as f:
            f.write(body)

        # exit(0)

def main():

    gt_data = get_gt_data_euroc()

    print(gt_data)

    save_gt_data_euroc(gt_data)

if __name__ == '__main__':
    main()
