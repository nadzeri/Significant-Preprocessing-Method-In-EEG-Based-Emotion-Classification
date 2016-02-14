function [datasets,label] = getTwoClass(datasets,label)
    idx = (label(:)~=2);
    label = label(idx);
    datasets = datasets(idx,:);
end