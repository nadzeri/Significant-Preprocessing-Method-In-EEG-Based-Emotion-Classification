function kelas = predictClassification(feature,datasets,label,method)
    TrainingSet=datasets; 
    TestSet=feature; 
    GroupTrain=label; 

    if strcmp(method,'svm')
        svmStruct = svmtrain(TrainingSet,GroupTrain);
        kelas = svmclassify(svmStruct,TestSet);
    elseif strcmp(method,'knn')
        kelas = kNN(TrainingSet, GroupTrain, TestSet, 3);
    end
end