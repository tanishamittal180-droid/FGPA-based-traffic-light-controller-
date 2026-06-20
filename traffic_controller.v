module traffic_controller(

input clk,
input reset,

input pedestrian,
input emergency,

input veh_NS,
input veh_EW,

output reg [2:0] NS,
output reg [2:0] EW,

output reg WALK,

output reg ERROR,

output reg [3:0] countdown,

output reg [7:0] cars_count,
output reg [7:0] ped_count,
output reg [7:0] emergency_count

);

parameter S0=3'b000;
parameter S1=3'b001;
parameter S2=3'b010;
parameter S3=3'b011;
parameter S4=3'b100;
parameter S5=3'b101;

reg [2:0] state;
reg [3:0] count;


always @(posedge clk or posedge reset)

begin

if(reset)

begin

state<=S0;
count<=0;

cars_count<=0;
ped_count<=0;
emergency_count<=0;

ERROR<=0;

end

else

begin

count<=count+1;


if(emergency)

begin

state<=S5;

count<=0;

emergency_count<=emergency_count+1;

end


else

begin

case(state)

S0:
begin

countdown<=5-count;

if(veh_NS)
cars_count<=cars_count+1;

if(count==5)

begin
state<=S1;
count<=0;
end

end


S1:

begin

countdown<=2-count;

if(count==2)

begin
state<=S2;
count<=0;
end

end


S2:

begin

countdown<=5-count;

if(veh_EW)
cars_count<=cars_count+1;

if(count==5)

begin
state<=S3;
count<=0;
end

end


S3:

begin

countdown<=2-count;

if(count==2)

begin

if(pedestrian)

state<=S4;

else

state<=S0;

count<=0;

end

end


S4:

begin

WALK<=1;

countdown<=4-count;

if(pedestrian)
ped_count<=ped_count+1;

if(count==4)

begin

state<=S0;
count<=0;

end

end


S5:

begin

countdown<=0;

if(!emergency)

begin

state<=S0;
count<=0;

end

end


endcase

end

end

end



always @(*)

begin

WALK=0;

case(state)

S0:
begin
NS=3'b001;
EW=3'b100;
end


S1:
begin
NS=3'b010;
EW=3'b100;
end


S2:
begin
NS=3'b100;
EW=3'b001;
end


S3:
begin
NS=3'b100;
EW=3'b010;
end


S4:
begin
NS=3'b100;
EW=3'b100;
WALK=1;
end


S5:
begin
NS=3'b001;
EW=3'b100;
end


default:
begin
NS=3'b100;
EW=3'b100;
end

endcase


// Safety Check

if(NS==3'b001 && EW==3'b001)

begin

ERROR=1;

NS=3'b100;
EW=3'b100;

end

else

ERROR=0;


end

endmodule