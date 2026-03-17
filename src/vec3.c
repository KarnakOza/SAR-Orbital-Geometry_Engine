#include <math.h>
#include "vec3.h"

Vec3 vec3_add(Vec3 a, Vec3 b)
{
    Vec3 r;
    r.x = a.x + b.x;
    r.y = a.y + b.y;
    r.z = a.z + b.z;
    return r;
}

Vec3 vec3_sub(Vec3 a, Vec3 b)
{
    Vec3 r;
    r.x = a.x - b.x;
    r.y = a.y - b.y;
    r.z = a.z - b.z;
    return r;
}

double vec3_dot(Vec3 a, Vec3 b)
{
    return a.x*b.x + a.y*b.y + a.z*b.z;
}

double vec3_norm(Vec3 v)
{
    return sqrt(v.x*v.x + v.y*v.y + v.z*v.z);
}
