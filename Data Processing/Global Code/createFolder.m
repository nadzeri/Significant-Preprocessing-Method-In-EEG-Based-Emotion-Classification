function createFolder(total_folder,path)
    mkdir(path);
    for i = 1:total_folder
        mkdir(strcat(path,'\',sprintf('S%02d',i)));
    end
end