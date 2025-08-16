# 1) Web Scraping for first 10 records from List of FIFA World Cup Finals
![FIFA World Cup Data Extraction Flow](https://github.com/user-attachments/assets/df5e5eec-c4b2-44c1-831b-da5589e52d7b)

## Steps:
1) Intsall requirements.txt
2) run fifaselenium.py
3) Copy Json data and call Google Excel API using Postman
4) Data will be extracted to mentioned excel sheet


# 2) Automate Naukri Profile Resume update 

## Steps:
1) Intsall requirements.txt
2) Update NAUKRI_EMAIL, NAUKRI_PASSWORD and RESUME_PATH with your details in **naukri_update.py**
3) Update "path-of-folder-having-naukri_update.py" and <env-name\> with your details in **naukri_update.bat**
4) File structure to be used:
   - **Project (Folder)** 
     - env-name 
       - Scripts 
        - python.exe
     - naukri_update.py
     - update_naukri.bat

5) Steps to Add Your .bat to Windows Task Scheduler
   - **Open Task Scheduler**: Press Win + R, type taskschd.msc, hit Enter.
   - **Create a New Task**: In the right panel, click Create Basic Task.
   - **Give it a name** like Update Naukri Resume.
   - **Set the Trigger**: Choose Daily (or Weekly if you want).
   - **Pick the time** you want it to run (e.g., 9:00 AM).
   - **Set the Action**: Select Start a Program.
   - Browse and select your update_naukri.bat file inside Project folder.
   - Finish & Save
   
7) Resume will be udated routinely as per the details. To test right click on task and select **Run**
