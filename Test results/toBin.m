function [ out ] = toBin( cal_num,in )

temp = fliplr(de2bi(in(cal_num(1)*100+1:(cal_num(end)+1)*100),12));
out = num2str(temp,'%d');
end

