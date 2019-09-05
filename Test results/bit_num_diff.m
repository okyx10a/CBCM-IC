function [ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff( cal_num,in )
bit_dif = zeros(1,100*length(cal_num));
num_dif = zeros(1,100*length(cal_num));
bit_dif_avg = zeros(0,length(cal_num));
num_dif_avg = zeros(0,length(cal_num));
num_dif_max = zeros(0,length(cal_num));
num_dif_min = zeros(0,length(cal_num));
in_bin = fliplr(de2bi(in(cal_num(1)*100+1:(cal_num(end)+1)*100),12));

%bit difference
for i = cal_num
    temp = in_bin(i*100+1:(i+1)*100,:);
    for j = 1:100
        bit_dif(100*(i-cal_num(1))+j) = sum(abs(temp(j,:)-temp(1,:)));
    end
    bit_dif_avg(i-cal_num(1)+1) = sum(bit_dif(100*(i-cal_num(1))+1:100*(i-cal_num(1)+1)))/100;  
end

%numerical difference
for i = cal_num
    temp = in(i*100+1:(i+1)*100);
    for j = 1:100
        num_dif(100*(i-cal_num(1))+j) = sum(temp(j)-temp(1));
    end
    num_dif_avg(i-cal_num(1)+1) = sum(num_dif(100*(i-cal_num(1))+1:100*(i-cal_num(1)+1)))/100;  
    num_dif_max(i-cal_num(1)+1) = max(temp);
    num_dif_min(i-cal_num(1)+1) = min(temp);
end

end

