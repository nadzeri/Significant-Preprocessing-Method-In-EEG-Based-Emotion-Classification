function [swa,swd] = ownSWT(A,level,wname)
    [h,g]=wfilters(wname,'r');
    wLength = length(h)/2-1;

    L = size(A,2);
    for i=1:level
        shift = 2^(i-1);
        start = L-(shift*wLength)+1;
        if(i==1)
            decompose = A;
        else
            decompose = swa(i-1,:);
        end

        for j=1:L
            swa(i,j)=0;
            swd(i,j)=0;
            shiftIdx=start;
            for k=1:length(h)
                swa(i,j)=swa(i,j)+decompose(shiftIdx)*h(k);
                swd(i,j)=swd(i,j)+decompose(shiftIdx)*g(k);
                shiftIdx=shiftIdx+shift;
                if(shiftIdx>L)
                    shiftIdx=shiftIdx-L;
                end
            end
            start=start+1;
            if(start>L)
                start=start-L;
            end
        end
    end
end