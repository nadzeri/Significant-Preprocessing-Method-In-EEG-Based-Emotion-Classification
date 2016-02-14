function raw_data = cutDataPredict(file_path)
    normRows = @(XXX) bsxfun(@times,XXX,1 ./ sqrt(sum(XXX.^2,2))); %Normalisasi Euclidean
    len1 = 640;
    
    dataEEG = csvread(file_path,1,0);
    start = mod(length(dataEEG),4)+1;
    dataEEG = dataEEG(start:end,3:16);
    L = length(dataEEG);

    if L>=len1
        used = (L - len1)/2;
    end

    start = used+1;
    stop = L - used;

    raw_data = transpose(dataEEG(start:stop,:)); 
    %raw_data = normRows(raw_data);
    
    for i=1:14
        path = strcat('../../Web App/img/raw_data/',num2str(i),'.png');

        set(gcf,'Visible','off');
        plot(raw_data(i,:));
        print(path,'-dpng');
    end
end