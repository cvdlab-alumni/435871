// FLOORS
myOBJloader("loft_floor", "loft_floor3", "loft_floor3", -0.2, 10, 4,6);
myOBJloader("lounge_floor", "floor_marble1", false, 0, 100, 2,3);
myOBJloader("corridor_floor", "floor_marble1", false, 0, 100, 5.2,1.5);
myOBJloader("myroom_floor", "parquet_orange", "parquet_orange", -0.05, 50, 2,3);
myOBJloader("bedroom_floor", "parquet_orange", "parquet_orange", -0.05, 50, 2,3);
myOBJloader("bathroom_floor", "bathroom_floor", "bathroom_floor-bump", 0.15, 200, 8,6);
myOBJloader("kitchen_floor", "kitchen_floor", "kitchen_floor-bump", 0.1, 100, 10,10);
myOBJloader("outside_floor", "floor_marble2", false, 0, 150, 2,2);

// WALLS
var wws = 10; // white wall shininess
var wwb = -0.2; // white wall bumpmap
// LOUNGE
myOBJloader("lounge_wall_left", "wall_white", "wall_white", wwb, wws, 8,4);
myOBJloader("lounge_wall_top", "wall_white", "wall_white", wwb, wws, 5,4);
myOBJloader("lounge_wall_right", "wall_white", "wall_white", wwb, wws, 6,4);
// BATHROOM and CORRIDOR
myOBJloader("bathroom_wall_top_bottom", "wall_white", "wall_white", wwb, wws, 4,4);
myOBJloader("bathroom_wall_rx_lx_corridor_rx", "wall_white", "wall_white", wwb, wws, 3,4);

myOBJloader("corridor_wall_bottom", "wall_white", "wall_white", wwb, wws, 10,4);
myOBJloader("corridor_wall_top", "wall_white", "wall_white", wwb, wws, 6,4);

// MY ROOM, BEDROOM, KITCHEN, ELEVATOR, OUTSIDE
myOBJloader("myroom_bedroom_kitchen_elevator_outside", "wall_white", "wall_white", wwb, wws, 4,4);

// EXTERNAL
myOBJloader("external_wall_top1", "wall_external", "wall_external-bump", wwb, wws, 18,4);
myOBJloader("external_wall_top2", "wall_external", "wall_external-bump", wwb, wws, 7,4);
myOBJloader("external_wall_left1", "wall_external", "wall_external-bump", wwb, wws, 8,4);
myOBJloader("external_wall_left2", "wall_external", "wall_external-bump", wwb, wws, 12,4);
myOBJloader("external_wall_bottom1", "wall_external", "wall_external-bump", wwb, wws, 11,4);
myOBJloader("external_wall_bottom2", "wall_external", "wall_external-bump", wwb, wws, 8,4);
myOBJloader("external_wall_bottom3", "wall_external", "wall_external-bump", wwb, wws, 8,2);
myOBJloader("external_wall_right1", "wall_external", "wall_external-bump", wwb, wws, 10,4);
myOBJloader("external_wall_right2", "wall_external", "wall_external-bump", wwb, wws, 8,2);

// DETAILS
myOBJloader("floor_doors", "floor_doors", false, 0, 100, 2,1);
myOBJloader("loft_marble", "loft_marble", false, 0, 10, 18,1);
myOBJloader("loft_entrance_marble", "loft_marble", false, 0, 10, 2,1);
myOBJloader("edges_loft", "edges_loft", "edges_loft", -0.2, 10, 8,1);
myOBJloader("edges_marble", "edges_marble", false, 0, 100, 6,1);
myOBJloader("edges_parquet", "edges_parquet", false, 0, 50, 5,1);
myOBJloader("white_jambs", "wall_white", "wall_white", -0.1, wws, 0.5,4);
myOBJloader("white_jambs_windows", "wall_white", "wall_white", -0.1, wws, 0.5,3);

// DOORS JAMB (stipite)
myOBJloader("doors_jamb", "doors_jamb", false, 0, 50, 1,5);
