function [xICA] = ownFastICA(X,r)

    %%%%%%%%%% Initial Variable %%%%%%%%%%
    eps = 1e-6;         % Convergence criteria
    maxIters = inf;     % Maximum # iterations
    normRows = @(XXX) bsxfun(@times,XXX,1 ./ sqrt(sum(XXX.^2,2))); %Normalisasi Euclidean
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%

    %%%%%%%%%% Centering %%%%%%%%%%
    % Compute sample mean
    meanEachRow = mean(X,2);
    % Subtract mean
    resultCentering = bsxfun(@minus,X,meanEachRow); %Binary singleton expansion function
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%

    %%%%%%%%%% Whitening %%%%%%%%%%
    % Compute sample covariance
    covMatrix = cov(resultCentering');
    % Whiten data
    [E,D,~] = svd(covMatrix,'econ'); %Singular Value Decomposition (E->EigenVector;D->EigenValue)
    resultWhitening = E * diag(1 ./ sqrt(diag(D))) * E' * resultCentering; %Main Whitening
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%

    %%%%%%%%%% Component Extraction %%%%%%%%%%
    % Random initial weights
    W = normRows(rand(r,size(resultWhitening,1)));
    %W = rand(r,size(resultWhitening,1));
    % Initial looping variable
    k = 0;
    err = inf;
    % Looping until convergen or until maxiter
    while (err > eps) && (k < maxIters)
        % Increment counter
        k = k + 1;

        % Update weights
        wLast = W; % Save last weights
        Sk = permute(wLast * resultWhitening,[1 3 2]);
        G = Sk .* exp(-0.5 * Sk.^2);
        Gp = Sk .* G;
        W = mean(bsxfun(@times,G,permute(resultWhitening,[3 1 2])),3) + bsxfun(@times,mean(Gp,3),wLast);
        W = normRows(W);

        % Decorrelate weights
        [U,S,~] = svd(W,'econ');
        W = U * diag(1 ./ diag(S)) * U' * W;

        % Update error
        err = max(1 - dot(W,wLast,2));
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    xICA = W * resultWhitening; 
    xICA = normRows(xICA);
end