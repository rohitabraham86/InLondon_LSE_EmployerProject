# This code file is used to extract the London Cycle Infrastructure Data
library(tidyverse)
install.packages("devtools")
devtools::install_github("PublicHealthDataGeek/CycleInfraLnd")
CycleInfraLnd.head
library(CycleInfraLnd)
?get_cid_lines

# Getting the cycling infrastructure database.
cid_asl = get_cid_lines(type = "advanced_stop_line")

cid_crs = get_cid_lines(type = "crossing")

cid_cycle_lanes = get_cid_lines(type = "cycle_lane_track")

cid_signal = get_cid_points(type = "signal")

cid_parking = get_cid_points(type = "cycle_parking")

cid_traf_calm = get_cid_points(type = "traffic_calming")


# Export the data as a CSV file.
write_csv(cid_cycle_lanes, file='cid_cycle_lanes.csv')

write_csv(cid_parking, file='cid_cid_parking.csv')

write_csv(cid_traf_calm, file='cid_traf_calm.csv')
