function divideFiveSeconds(dataset_path,project_path)
    addpath(genpath('..\Global Code'));
    normRows = @(XXX) bsxfun(@times,XXX,1 ./ sqrt(sum(XXX.^2,2))); %Normalisasi Euclidean
    
    base_path = strcat(project_path,'\EEG');
    base_path2 = strcat(project_path,'\USED_EEG');
    dataKuesioner = csvread(strcat(dataset_path,'\metadata\list questionnairre.csv'));
    
    counterNewKuesioner=1;
    counterKuesioner=1;
    newDataKuesioner={};
    allList = dir( base_path );
    allDir = { allList(3:end).name };
    lewat=0;
    
    if exist(base_path2, 'dir')
        system(strcat('rmdir /S /Q "',base_path2,'"'));
    end
    createFolder(length(allDir),base_path2);
    
    for i=1:length(allDir)
        dataOneDir = allDir{i};
        allFileList = dir(strcat(base_path,'\',dataOneDir));
        allFileName = { allFileList(3:end).name };

        counter=1;

        for j = 1:length(allFileName)
            dataOneFile = allFileName{j};
            dataEEG = csvread(strcat(base_path,'\',dataOneDir,'\',dataOneFile));
            %dataEEG = normRows(dataEEG);
            if length(dataEEG(1,:))==640
                csvwrite(strcat(base_path2,'\',dataOneDir,'\T',num2str(counter),'.csv'),dataEEG);
                newDataKuesioner{counterNewKuesioner} = dataKuesioner(counterKuesioner,:);
                counter=counter+1;
                counterKuesioner=counterKuesioner+1;
                counterNewKuesioner=counterNewKuesioner+1;
            elseif length(dataEEG(1,:))==3200
                start=1;
                stop=640;
                for k=1:5
                    csvwrite(strcat(base_path2,'\',dataOneDir,'\T',num2str(counter),'.csv'),dataEEG(:,start:stop));
                    newDataKuesioner{counterNewKuesioner} = dataKuesioner(counterKuesioner,:);
                    start=stop+1;
                    stop=stop+640;
                    counter=counter+1;
                    counterNewKuesioner=counterNewKuesioner+1;
                end
                counterKuesioner=counterKuesioner+1;
            else
                lewat=lewat+1;
            end
        end
    end
    newDataKuesioner = reshape(cell2mat(newDataKuesioner),2,[]);
    newDataKuesioner = transpose(newDataKuesioner);
    
    mkdir(strcat(project_path,'\Metadata'));
    
    csvwrite(strcat(project_path,'\Metadata\newDataKuesioner.csv'),newDataKuesioner);
end