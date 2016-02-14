
function [results] = kNN(TrainingSet,GroupTrain,TestSet,k)
    [L,L1] = size(TestSet);
    results = zeros(L);
    for i = 1:L
        [L2,L3] = size(TrainingSet);
        data_distance = zeros(L2);
        for j = 1:L2
            p = TrainingSet(j,:);
            q = TestSet(i,:);
            
            data_distance (j) = sum(abs(p-q)./(abs(p) + abs(q)));
        end
        
        [B,I] = sort(data_distance);
        
        nearest = GroupTrain(I(1:k));
        nearest_distance = B(1:k);
        sse = nearest_distance(1)/nearest_distance(2);
%         disp(sse);
%         disp(nearest);
        if sse<=0.97
            results(i)=nearest(1);
        else
            results(i)=mode(nearest);
        end
        %results(i)=mode(nearest);
    end
end

