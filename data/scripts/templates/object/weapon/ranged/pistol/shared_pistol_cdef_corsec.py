#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Weapon()

	result.template = "object/weapon/ranged/pistol/shared_pistol_cdef_corsec.iff"
	result.attribute_template_id = 10
	result.stfName("weapon_name","pistol_cdef_corsec")		
	
	#### BEGIN MODIFICATIONS ####
	####  END MODIFICATIONS  ####
	
	return result