#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Ship()

	result.template = "object/ship/base/shared_ship_transport_base.iff"
	result.attribute_template_id = -1
	result.stfName("space_ship","transport_base")		
	
	#### BEGIN MODIFICATIONS ####
	####  END MODIFICATIONS  ####
	
	return result