#include <stdio.h>
typedef struct {
	unsigned int uid; // owner id
	unsigned int gid; // group id
	unsigned char u;  // owner’s permission
	unsigned char g;  // group’s permission
	unsigned char o;  // other’s permission
} Permission;

int accesscheck(unsigned int uid, unsigned int gid, unsigned int p, int f)
{2
    // Is the file accessible?
    if (p <= 0) return 0; // deny
    // Creates a local copy of permission value
    Permission permission = getPermission(f);
    // First check if the user is owner of the file
    if (permission.uid == uid) {
        if ((permission.u & p) == p) { // Check to use if the user has the permission
            return 1; // grant
        } else {
            return 0; // deny
        }
    }
    // If the user is not the owner, check if user is part of the group that can access.
    else if (permission.gid == gid) {
        if ((permission.g & p) == p) { // Check to use if the user has the permission
            return 1; // grant
        } else {
            return 0; // deny
        }
    }
    // The user is not owner nor in the group, but could be with other's permission.
    else {
        if ((permission.o & p) == p) {
            return 1; // grant
        } else {
            return 0; // deny
        }
    }
}
int main(){
    return 0;
}