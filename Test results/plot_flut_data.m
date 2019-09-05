%% Setup
cal_num = 0:25;
figure(1)
xlabel('Calibration input value');
ylabel('Number of bit difference');
title('Average bit difference');
legend('-DynamicLegend');
hold all
figure(2)
xlabel('Calibration input value');
ylabel('Output value difference');
title('Average numerical difference');
legend('-DynamicLegend');
hold all
figure(3)
xlabel('Calibration input value');
ylabel('Output value');
title('Numerical variation range');
legend('-DynamicLegend');
hold all

%% left_res000_samp100
[ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff(cal_num,left_res000_samp100);
figure(1)
plot(cal_num,bit_dif_avg,'b','LineWidth',2,'DisplayName','left res000 samp100');
legend('off')
legend('show')
figure(2)
plot(cal_num,num_dif_avg,'b','LineWidth',2,'DisplayName','left res000 samp100');
legend('off')
legend('show')
figure(3)
plot(cal_num,num_dif_max,'b', cal_num,num_dif_min,'b','LineWidth',2,'DisplayName','left res000 samp100');
legend('off')
legend('show')
%% left_res111_samp100
[ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff(cal_num,left_res111_samp100);
figure(1)
plot(cal_num,bit_dif_avg,'r','LineWidth',2,'DisplayName','left res111 samp100');
legend('off')
legend('show')
figure(2)
plot(cal_num,num_dif_avg,'r','LineWidth',2,'DisplayName','left res111 samp100');
legend('off')
legend('show')
figure(3)
plot(cal_num,num_dif_max,'r', cal_num,num_dif_min,'r','LineWidth',2,'DisplayName','left res111 samp100');
legend('off')
legend('show')
%% right_res000_samp100_cs0
[ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff(cal_num,right_res000_samp100_cs0);
figure(1)
plot(cal_num,bit_dif_avg,'--m','LineWidth',2,'DisplayName', 'right res000 samp100 cs0');
legend('off')
legend('show')
figure(2)
plot(cal_num,num_dif_avg,'--m','LineWidth',2,'DisplayName', 'right res000 samp100 cs0');
legend('off')
legend('show')
figure(3)
plot(cal_num,num_dif_max,'--m',cal_num,num_dif_min,'--m','LineWidth',2 ,'DisplayName', 'right res000 samp100 cs0');
legend('off')
legend('show')
%% right_res000_samp100_cs1
[ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff(cal_num,right_res000_samp100_cs1);
figure(1)
plot(cal_num,bit_dif_avg,'g-o','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k','DisplayName','right res000 samp100 cs1');
legend('off')
legend('show')
figure(2)
plot(cal_num,num_dif_avg,'g-o','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k','DisplayName','right res000 samp100 cs1');
legend('off')
legend('show')
figure(3)
plot(cal_num,num_dif_max,'g-o', cal_num,num_dif_min,'g-o','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k','DisplayName','right res000 samp100 cs1');
legend('off')
legend('show')
%% right_res111_samp100_cs0
[ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff(cal_num,right_res111_samp100_cs0);
figure(1)
plot(cal_num,bit_dif_avg,'y:^','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k' ,'DisplayName','right res111 samp100 cs0');
legend('off')
legend('show')
figure(2)
plot(cal_num,num_dif_avg,'y:^','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k' ,'DisplayName','right res111 samp100 cs0');
legend('off')
legend('show')
figure(3)
plot(cal_num,num_dif_max,'y:^',cal_num,num_dif_min,'y:^','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k' ,'DisplayName','right res111 samp100 cs0');
legend('off')
legend('show')
%% right_res111_samp100_cs1
[ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff(cal_num,right_res111_samp100_cs1);
figure(1)
plot(cal_num,bit_dif_avg,'k-*','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k' ,'DisplayName','right res111 samp100 cs1');
legend('off')
legend('show')
figure(2)
plot(cal_num,num_dif_avg,'k-*','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k' ,'DisplayName','right res111 samp100 cs1');
legend('off')
legend('show')
figure(3)
plot(cal_num,num_dif_max,'k-*',cal_num,num_dif_min,'k-*','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'k' ,'DisplayName','right res111 samp100 cs1');
legend('off')
legend('show')
%% left_res000_samp100_pcb
[ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff(cal_num,left_res000_samp100_pcb);
figure(1)
plot(cal_num,bit_dif_avg,'r-s','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'r' ,'DisplayName','left res000 samp100 pcb');
legend('off')
legend('show')
figure(2)
plot(cal_num,num_dif_avg,'r-s','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'r' ,'DisplayName','left res000 samp100 pcb');
legend('off')
legend('show')
figure(3)
plot(cal_num,num_dif_max,'r-s',cal_num,num_dif_min,'r-s','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'r' ,'DisplayName','left res000 samp100 pcb');
legend('off')
legend('show')
%% left_res111_samp100_pcb
[ bit_dif,bit_dif_avg,num_dif,num_dif_avg,num_dif_max,num_dif_min] = bit_num_diff(cal_num,left_res111_samp100_pcb);
figure(1)
plot(cal_num,bit_dif_avg,'b-h','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'b' ,'DisplayName','left res111 samp100 pcb');
legend('off')
legend('show')
figure(2)
plot(cal_num,num_dif_avg,'b-h','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'b' ,'DisplayName','left res111 samp100 pcb');
legend('off')
legend('show')
figure(3)
plot(cal_num,num_dif_max,'b-h',cal_num,num_dif_min,'b-h','LineWidth',2 ,'MarkerSize',8,'MarkerFaceColor', 'b' ,'DisplayName','left res111 samp100 pcb');
legend('off')
legend('show')
