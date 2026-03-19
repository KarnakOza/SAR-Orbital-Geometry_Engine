#include <stdio.h>
#include <math.h>
#include "constants.h"
#include "sar_range.h"
#include "vec3.h"


double orbital_velocity(double altitude);
double orbital_period(double altitude);
double doppler_centroid(double velocity, double wavelength, double angle);

double slant_range(double xs, double ys, double zs,
                   double xg, double yg, double zg);

/*void satellite_position_eci(double a, double e, double i,
                            double raan, double omega, double nu,
                            double *x, double *y, double *z);  */


 /*ground.x = 6378.0;
    ground.y = 0;
    ground.z = 0; */


//x = 1000;
    //y = 2000;
    //z = 700000;
    //double xg = 6378.0;
    //double yg = 0.0;
    //double zg = 0.0;
