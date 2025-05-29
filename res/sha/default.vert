#version 420 core

layout (binding = 0) uniform UBO {
 mat4 view;
 mat4 projection;
} camera;

layout (location = 0) in vec3 vertex_position;

layout (location = 1) in vec3 instance_translation;
layout (location = 2) in vec3 instance_rotation;
layout (location = 3) in vec3 instance_scale;
layout (location = 4) in vec3 instance_colour;

out vec3 instance_fragment_colour;

mat4 translation_matrix(const vec3 v) {
	return mat4(
		1.0f, 0.0f, 0.0f, 0.0f,
		0.0f, 1.0f, 0.0f, 0.0f,
		0.0f, 0.0f, 1.0f, 0.0f,
		v.x , v.y , v.z , 1.0f
	);
}
mat4 scale_matrix(const vec3 v) {
	return mat4(
		v.x, 0.0, 0.0, 0.0,
		0.0, v.y, 0.0, 0.0,
		0.0, 0.0, v.z, 0.0,
		0.0, 0.0, 0.0, 1.0
	);
}

//For all relevant mathematical proofs relating to the following, refer to the paper I wrote at https://github.com/KrohnusMelavea/math-papers titled "Quaternions for Spacial Manipulation - Daniel de Waal"
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
 instance_fragment_colour = vec3(1, 1, 1);
 gl_Position = 
  camera.projection * 
  camera.view * 
  translation_matrix(instance_translation) * 
  quaternion_rotate_3d(
   scale_matrix(instance_scale) * vec4(vertex_position, 1.0), 
   instance_rotation
  );
}