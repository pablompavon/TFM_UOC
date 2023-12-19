# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 10:03:24 2023

@author: pablo
"""

import requests
import pandas as pd
import Reloxo
import os


#%% Listar archivos


def listar_files(repo_url, path='', token=''):
    api_url = f"{repo_url.rstrip('/').replace('github.com', 'api.github.com/repos')}/contents/{path}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        files = []
        for file_info in response.json():
            if file_info['type'] == 'file':
                files.append(file_info['path'])
            elif file_info['type'] == 'dir':
                files += listar_files(repo_url, file_info['path'], token)
        return files
    else:
        print(f"Fallo. Status code: {response.status_code}")
        return None
    

def leer_files(files_in_repo):
    if files_in_repo:
        print("Archivos listados:")
        for file in files_in_repo:
            print(file)
            

#%% Descargar archivo


def descargar_file(repo_url, filepath, token):
    tempo=Reloxo.ElapsedTimer()
    api_url = f"{repo_url.rstrip('/').replace('github.com', 'api.github.com/repos')}/contents/{filepath}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(api_url, headers=headers)
    download_url=response.json().get("download_url")
    response_file=requests.get(download_url)
    save_path=filepath.split("/")[-2].split("=")[-1]+".parquet"
    with open(save_path, 'wb') as file:
        file.write(response_file.content)
    pd.read_parquet(save_path, engine='pyarrow').sort_values(by=["unix"]).to_csv(save_path.split(".")[0]+'.csv')
    os.remove(save_path)
    print("ARQUIVO %s DESCARGADO...(%s)" % (save_path, tempo.elapsed_time()))
    
    
