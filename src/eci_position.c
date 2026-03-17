#include <stdio.h>
#include <math.h>
#include "constants.h"
#include "vec3.h"

Vec3 satellite_position_eci(double a,double e,double i,
                             double raan,double omega,double nu)
{
    Vec3 pos;
    double r;

    r = (a*(1-e*e))/(1+e*cos(nu));

    pos.x = r*(cos(raan)*cos(omega+nu)
          - sin(raan)*sin(omega+nu)*cos(i));

    pos.y = r*(sin(raan)*cos(omega+nu)
          + cos(raan)*sin(omega+nu)*cos(i));

    pos.z = r*(sin(omega+nu)*sin(i));

    return pos;
}
