#version 430

layout (binding = 0) uniform UBO {
 vec4 translation;  /* Question 2: Camera-Based Translation */
 vec4 rotation;     /* Question 3: Camera-Based Rotation    */
 vec4 global_scale; /* Question 4" Global Scalings */
 mat4 projection;
} camera;

layout (location = 0) in vec3 vertex_position; /* Question 1: Vertex Data */

layout (location = 1) in vec3 instance_translation; /* Question 2: Instance-Based Translation */
layout (location = 2) in vec3 instance_rotation;    /* Question 3: Instance-Based Rotation    */
layout (location = 3) in vec3 instance_scale;       /* Question 4: Instance-Based Scaling     */

/* Question 2: Translation */
mat4 translation_matrix(const vec3 v) {
	return mat4(
		1.0f, 0.0f, 0.0f, 0,
		0.0f, 1.0f, 0.0f, 0,
		0.0f, 0.0f, 1.0f, 0,
		v.x, v.y, v.z, 1.0f
	);
}
/* Question 4: Scaling */
mat4 scale_matrix(const vec3 v) {
	return mat4(
		v.x, 0.0, 0.0, 0.0,
		0.0, v.y, 0.0, 0.0,
		0.0, 0.0, v.z, 0.0,
		0.0, 0.0, 0.0, 1.0
	);
}

/* 
Question 3: Rotation
For all relevant mathematical proofs relating to the following, 
refer to the paper I wrote at https://github.com/KrohnusMelavea/math-papers,
titled "Quaternions for Spacial Manipulation - Daniel de Waal" 
*/
vec4 quaternion_rotate_3d(const vec4 V, const vec3 A) {
	const float cx = cos(A.x), cy = cos(A.y), cz = cos(A.z);
	const float sx = sin(A.x), sy = sin(A.y), sz = sin(A.z);
	const float x = V.x, y = V.y, z = V.z;
	return vec4(
		(x*cy + (y*sx + z*cx) * sy) * cz - (y*cx - z*sx) * sz,
		(x*cy + (y*sx + z*cx) * sy) * sz + (y*cx - z*sx) * cz,
		(y*sx + z*cx) * cy - x*sy,
		1.0
	);
}

void main() {
 const vec4 object_transformation = 
  /* Question 2: Instance-Based Translation */
  translation_matrix(instance_translation) *
  /* Question 3: Instance-based Rotation */
  quaternion_rotate_3d(
   /* Question 4: Instance-Based Scaling */
   scale_matrix(instance_scale) * 
   vec4(vertex_position, 1.0), 
   instance_rotation
  );

 gl_Position = 
  camera.projection * 
  /* Question 3: Camera-Based Rotation */
  quaternion_rotate_3d(
   /* Question 2: Camera-Based Translation */
   translation_matrix(camera.translation.xyz) *
   /* Question 4: Global Scaling */
   scale_matrix(camera.global_scale.xyz) * 
   object_transformation,
   camera.rotation.xyz
  );
}