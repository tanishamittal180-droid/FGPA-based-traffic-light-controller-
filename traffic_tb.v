`timescale 1ns/1ps

module traffic_tb();

reg clk;
reg reset;

reg pedestrian;
reg emergency;

reg veh_NS;
reg veh_EW;

wire [2:0] NS;
wire [2:0] EW;

wire WALK;
wire ERROR;

wire [3:0] countdown;

wire [7:0] cars_count;
wire [7:0] ped_count;
wire [7:0] emergency_count;



traffic_controller DUT(

.clk(clk),
.reset(reset),

.pedestrian(pedestrian),
.emergency(emergency),

.veh_NS(veh_NS),
.veh_EW(veh_EW),

.NS(NS),
.EW(EW),

.WALK(WALK),
.ERROR(ERROR),

.countdown(countdown),

.cars_count(cars_count),
.ped_count(ped_count),
.emergency_count(emergency_count)

);


// Clock generation

always #5 clk = ~clk;



// Test sequence

initial
begin

clk = 0;

reset = 1;

pedestrian = 0;
emergency = 0;

veh_NS = 0;
veh_EW = 0;


#20
reset = 0;


// Heavy traffic at NS road

#50
veh_NS = 1;

#60
veh_NS = 0;


// Heavy traffic at EW road

#100
veh_EW = 1;

#60
veh_EW = 0;


// Pedestrian request

#100
pedestrian = 1;

#20
pedestrian = 0;


// Emergency vehicle

#100
emergency = 1;

#50
emergency = 0;


// Finish simulation

#500
$finish;

end



// Generate VCD

initial
begin

$dumpfile("traffic.vcd");

$dumpvars(0,traffic_tb);

end



// Monitor outputs

initial
begin

$monitor(

"Time=%0t State=%d Count=%d NS=%b EW=%b WALK=%b ERROR=%b Cars=%d Ped=%d Emergency=%d",

$time,
DUT.state,
DUT.count,

NS,
EW,

WALK,
ERROR,

cars_count,
ped_count,
emergency_count

);

end

endmodule