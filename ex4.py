# -*- coding: utf-8 -*-
#车辆赋值
cars = 100
#车子的容量赋值
space_in_a_car = 4.0
#驾驶员赋值
drivers = 30
#乘客赋值
passengers = 90
#定义变量
cars_not_driven = cars -drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven
#输出可用车辆
print "There are",cars,"cars available."
#输出可用的驾驶员
print "There are only", drivers, "drivers available."
#输出没有使用的车辆
print "There will be",cars_not_driven, "empty cars today."
#输出拼车容量
print "We can transport", carpool_capacity,"people today."
#输出今天的乘客容量
print "We have", passengers, "to carpool today."
#输出每辆车平均载客人数
print "We need to put about", average_passengers_per_car,"in each car."
