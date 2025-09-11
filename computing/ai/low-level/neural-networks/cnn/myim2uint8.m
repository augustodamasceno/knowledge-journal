function u8 = myim2uint8(img)
imin = min(img(:));
imax = max(img(:));
if imax == imin
    u8 = uint8(zeros(size(img)));
else
    img = (img - imin) / (imax - imin);   % 0–1
    u8  = uint8(round(img * 255));        % 0–255
end
end