function [xFFT] = ownFFT(X)
    X = double(X);
    N = length(X);
    n = 0:N-1;
    k = n';
    M = exp(-2j*pi*k*n/N);
    %disp(M);
    xFFT = (M*X')';
end