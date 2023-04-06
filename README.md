---
title: CS485 Milestone 2
emoji: 🏢
colorFrom: red
colorTo: blue
sdk: streamlit
sdk_version: 1.17.0
app_file: test-app.py
pinned: false
---

# CS482-Fine_Tuning_Language_Models

I elected to use an Anaconda Virtual Environment, although that decision will likely change in the near future.

If you don't have Anaconda installed you can download it from here: https://docs.anaconda.com/anaconda/install/index.html

With Anaconda installed, we then make a new conda environment using the command "conda create --name your_env_name"

https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

We then intall the following packages:  

-----PyTorch
   
-----Transformers
  
I already have PyTorch installed, but to download PyTorch into your Conda virtual environment activate your 
virtual environment using the command "conda activate your_env_name"

then run the command "conda install pytorch torchvision torchaudio -c pytorch"

For Transformers you can use the command "conda install -c conda-forge transformers" (REMEMBER TO
INSTALL PACKAGES IN YOUR VIRTUAL ENVIRONMENT ONLY)

I did not have Transformers installed yet, so below is a screenshot of me downloading and installing
the package into my Conda Virtual Environment called "base"

<img width="595" alt="Screen Shot 2023-03-26 at 8 45 42 PM" src="https://user-images.githubusercontent.com/62716243/227816988-b945cb49-54a4-47cc-8f02-50f2d5d287c7.png">

Below are screenshots that confirm PyTorch and Transformers are installed in the Conda environment "base"


<img width="536" alt="Screen Shot 2023-03-26 at 8 44 42 PM" src="https://user-images.githubusercontent.com/62716243/227817071-ee3e2f70-21b4-4100-b4f3-5c963608aa61.png">
<img width="428" alt="Screen Shot 2023-03-26 at 8 44 23 PM" src="https://user-images.githubusercontent.com/62716243/227817073-698df191-beab-48ea-bb48-4f46073577fd.png">
