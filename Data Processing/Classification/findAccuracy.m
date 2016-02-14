function [jmlBenar,rata_rata,tp,tn,fp,fn] = findAccuracy(datasets,label,method)
    jmlData = length(label);
    %jmlTest = 20;

    tp = 0;
    fn = 0;
    fp = 0;
    tn = 0;
    
    indices = crossvalind('Kfold',jmlData,10);
    for h = 1:10
        test = (indices == h); train = ~test;
        jmlTest = sum(test);
        TrainingSet=datasets(train,:); 
        TestSet=datasets(test,:); 
        GroupTrain=label(train);
        dataAsli = label(test);  
        
        if strcmp(method,'svm')
            svmStruct = svmtrain(TrainingSet,GroupTrain,'kernel_function','rbf');
            results = svmclassify(svmStruct,TestSet);
        elseif strcmp(method,'knn')
            results = kNN(TrainingSet, GroupTrain, TestSet, 3);
        end

        jmlBenar(h) = 0;
        for i = 1:jmlTest
            if(dataAsli(i)==results(i))
                if dataAsli(i)==3
                    tp=tp+1;
                else
                    tn=tn+1;
                end
                jmlBenar(h)=jmlBenar(h)+1;
            else
                if results(i)==3
                    fp=fp+1;
                else
                    fn=fn+1;
                end
            end 
        end
        jmlBenar(h) = jmlBenar(h)/jmlTest;
    end
    rata_rata = mean2(jmlBenar);
end