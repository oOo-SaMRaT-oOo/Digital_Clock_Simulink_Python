out = sim("Clock_Model.slx");
So = out.So;
St = out.St;
Mo = out.Mo;
Mt = out.Mt;
Ho = out.Ho;
Ht = out.Ht;
t = out.tout;
save("clock_data.mat","So","St","t","Ho","Ht","Mo","Mt");