import os, sys, time


def createMovieStructure(projectName: str) -> None:

    if os.path.isdir(projectName):
            print (f'Warrning! Project <<< {projectName.upper()} >>> Exist! Try agin...')
            time.sleep(3)
            sys.exit(0)
    else:
        projectLibrary: str= os.path.join(projectName,'___PROJECT.LIBRARY___')
        os.makedirs(projectLibrary, exist_ok=True)
        
    mainSubFolder: str=['_SOURCES',
                        '_VFX',
                        '_COLOUR',
                        '_GPHX',
                        '_METADATAS',
                        '_RENDER.CACHES',
                        '_DELIVERIES',
                        '_RESOLVE_PROJECT'
                        ]
    videoSourcesFolders: list = ['VIDEO', ['Camera.Cards', 'Proxies', 'Misc'] ]
    AudioSourceFolders : list =['AUDIO', ['Master.Audio', 'Music', 'SoundFX', 'VOIC']]
    ClourVFXSourceFolders : list =['For.Who', 'From.Who', 'Misc']
    GPHXSourceFolders : list =['AfterEffects', 'Photoshop', 'Render', 'Misc'] 
    MetaDataSourceFoldersFOR : list =['For.Who',['Sync', 'TimeLine']] 
    MetaDataSourceFoldersFROM : list =['From.Who',['Sync', 'TimeLine']] 
    DeliverySourceFolder : list = ['Final.Master', 'Final', 'Current', 'Old']

    index=0
    for folder in mainSubFolder:
        mainStructure: str = os.path.join(projectName,f'{0}{index}{folder}')
        os.makedirs(mainStructure, exist_ok=True)
        index+=1

    #videoSourcesFolders
    for item in range(1):
        for i in range(1):
            for j in range(3):
                pathString: str=fr'{videoSourcesFolders[item]}\0{j}_{videoSourcesFolders[i+1][j]}'
                PATH: str = os.path.join(projectName,'00_SOURCES',pathString)
                os.makedirs(PATH, exist_ok=True)

    #AudioSourceFolders
    for item in range(1):
        for i in range(1):
            for j in range(4):
                pathString: str=fr'{AudioSourceFolders[item]}\0{j}_{AudioSourceFolders[i+1][j]}'
                PATH: str = os.path.join(projectName,'00_SOURCES',pathString)
                os.makedirs(PATH, exist_ok=True)

    #VFXSourceFolders
    for i in range(3):
        pathString: str = fr'{ClourVFXSourceFolders[i]}'
        PATH: str = os.path.join(projectName,'01_VFX',pathString)
        os.makedirs(PATH, exist_ok=True)

    #ColourSourceFolders
    for i in range(3):
        pathString: str = fr'{ClourVFXSourceFolders[i]}'
        PATH: str = os.path.join(projectName,'02_COLOUR',pathString)
        os.makedirs(PATH, exist_ok=True)
    
    #GPHXSourceFolders   
    for i in range(4):
        pathString: str = fr'{GPHXSourceFolders[i]}'
        PATH: str = os.path.join(projectName,'03_GPHX',pathString)
        os.makedirs(PATH, exist_ok=True)

    for item in range(1):
        for i in range(1):
            for j in range(2):
                pathString: str=fr'{MetaDataSourceFoldersFOR[item]}\0{j}_{MetaDataSourceFoldersFOR[i+1][j]}'
                PATH: str = os.path.join(projectName,'04_METADATAS',pathString)
                os.makedirs(PATH, exist_ok=True) 

    for item in range(1):
        for i in range(1):
            for j in range(2):
                pathString: str=fr'{MetaDataSourceFoldersFROM[item]}\0{j}_{MetaDataSourceFoldersFROM[i+1][j]}'
                PATH: str = os.path.join(projectName,'04_METADATAS',pathString)
                os.makedirs(PATH, exist_ok=True) 

    #DeliverySourceFolder
    for i in range(4):
        pathString: str = fr'{DeliverySourceFolder[i]}'
        PATH: str = os.path.join(projectName,'06_DELIVERIES',pathString)
        os.makedirs(PATH, exist_ok=True)
        
    print(f'Congratulations! project <<< {projectName.upper()} >>> was successfully built...')
    time.sleep(3)
    sys.exit(0)
        






def createEpisodicStructure(projectName: str, epizodCount: int) -> None:
    if os.path.isdir(projectName):
            print (f'Warrning! Project <<< {projectName.upper()} >>> Exist! Try agin...')
            time.sleep(3)
            sys.exit(0)
    else:
        projectLibrary: str= os.path.join(projectName,'___PROJECT.LIBRARY___')
        os.makedirs(projectLibrary, exist_ok=True)
    
    videoSourcesFolders: list = ['VIDEO', ['Camera.Cards', 'Proxies', 'Misc'] ]
    AudioSourceFolders : list =['AUDIO', ['Master.Audio', 'Music', 'SoundFX', 'VOIC']]
    ClourVFXSourceFolders : list =['For.Who', 'From.Who', 'Misc']
    GPHXSourceFolders : list =['AfterEffects', 'Photoshop', 'Render', 'Misc'] 
    MetaDataSourceFoldersFOR : list =['For.Who',['Sync', 'TimeLine']] 
    MetaDataSourceFoldersFROM : list =['From.Who',['Sync', 'TimeLine']] 
    DeliverySourceFolder : list = ['Final.Master', 'Final', 'Current', 'Old']
    
    for num in range(epizodCount):
        rootPathString: str=fr'{projectName}\EPISODE__{num+1}'
        os.makedirs(rootPathString, exist_ok=True)
        #videoSourcesFolders
        for item in range(1):
            for i in range(1):
                for j in range(3):
                    pathString: str=fr'{videoSourcesFolders[item]}\0{j}_{videoSourcesFolders[i+1][j]}'
                    PATH: str = os.path.join(rootPathString,'00_SOURCES',pathString)
                    os.makedirs(PATH, exist_ok=True)
        #AudioSourceFolders
        for item in range(1):
            for i in range(1):
                for j in range(4):
                    pathString: str=fr'{AudioSourceFolders[item]}\0{j}_{AudioSourceFolders[i+1][j]}'
                    PATH: str = os.path.join(rootPathString,'00_SOURCES',pathString)
                    os.makedirs(PATH, exist_ok=True)

        #VFXSourceFolders
        for i in range(3):
            pathString: str = fr'{ClourVFXSourceFolders[i]}'
            PATH: str = os.path.join(rootPathString,'01_VFX',pathString)
            os.makedirs(PATH, exist_ok=True)

        #ColourSourceFolders
        for i in range(3):
            pathString: str = fr'{ClourVFXSourceFolders[i]}'
            PATH: str = os.path.join(rootPathString,'02_COLOUR',pathString)
            os.makedirs(PATH, exist_ok=True)
        
        #GPHXSourceFolders   
        for i in range(4):
            pathString: str = fr'{GPHXSourceFolders[i]}'
            PATH: str = os.path.join(rootPathString,'03_GPHX',pathString)
            os.makedirs(PATH, exist_ok=True)

        for item in range(1):
            for i in range(1):
                for j in range(2):
                    pathString: str=fr'{MetaDataSourceFoldersFOR[item]}\0{j}_{MetaDataSourceFoldersFOR[i+1][j]}'
                    PATH: str = os.path.join(rootPathString,'04_METADATAS',pathString)
                    os.makedirs(PATH, exist_ok=True) 

        for item in range(1):
            for i in range(1):
                for j in range(2):
                    pathString: str=fr'{MetaDataSourceFoldersFROM[item]}\0{j}_{MetaDataSourceFoldersFROM[i+1][j]}'
                    PATH: str = os.path.join(rootPathString,'04_METADATAS',pathString)
                    os.makedirs(PATH, exist_ok=True) 

        #DeliverySourceFolder
        for i in range(4):
            pathString: str = fr'{DeliverySourceFolder[i]}'
            PATH: str = os.path.join(rootPathString,'06_DELIVERIES',pathString)
            os.makedirs(PATH, exist_ok=True)
        
        #RenderCacheFolder
        for i in range(4):
            pathString: str = fr'{DeliverySourceFolder[i]}'
            PATH: str = os.path.join(rootPathString,'05_RENDER.CACHES')
            os.makedirs(PATH, exist_ok=True)
        
        #DRPSFolder
        for i in range(4):
            pathString: str = fr'{DeliverySourceFolder[i]}'
            PATH: str = os.path.join(rootPathString,'07_RESOLVE_PROJECT')
            os.makedirs(PATH, exist_ok=True)
        
            
    print(f"Congratulations! project <<< {projectName.upper()}  >>> with <<{epizodCount}>> Episode's was successfully built...")
    time.sleep(3)
    sys.exit(0)
















if __name__ == '__main__' :
    aboutMessage : str = '''
    Welcome to daVinci Resolve Studio Project Organizer. 
    This utility organize multiple episodes and edits in a Resolve Project
    version 1.0
    
    Copyright (C) 2003-2024 Ahad Mohebbi
    Developed by Ahad Mohebbi [ mohebbi.ahad@gmail.com ] 
    https://github.com/ahadmohebbi

    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation.
    '''
    print(aboutMessage)
    print(75*'-',end='\n')
    print('\n')

    while True:
        try:
            projectType: int = int(input("What is your project type? 1=Edit | 2=Episode (Ctrl+C=Exit): "))
            if projectType == 1:
                while True:
                    try:
                        print('You select the <EDIT> project ... Now enter your project name...', end='\n')
                        ProjectName: str = input("What is your project name? ")
                        createMovieStructure(ProjectName)
                        break
                    except ValueError:
                        print('Please enter project name as string...')
                    except KeyboardInterrupt :
                        print('\nYou exited the program by pressing CTRL+C')
                        time.sleep(3)
                        sys.exit(0)
            
            elif projectType == 2:
                while True:
                    try:
                        print('You select the <Episodic> project ... Now enter your project name...', end='\n')
                        ProjectName: str = input("What is your project name? ")
                        epizodCount: int = int(input("How many episode's do you plan to work on? "))
                        createEpisodicStructure(ProjectName, epizodCount)
                        break
                    except ValueError:
                        print('Please enter an integer value ...')
                    except KeyboardInterrupt :
                        print('\nYou exited the program by pressing CTRL+C')
                        time.sleep(3)
                        sys.exit(0)
            else:
                continue
            break
        except ValueError :
            print('Please enter number 1 -> Edit  |  2 -> Episode')
        except KeyboardInterrupt :
            print('\nYou exited the program by pressing CTRL+C')
            time.sleep(3)
            sys.exit(0)


