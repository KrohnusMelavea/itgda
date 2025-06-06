#version 430

layout (binding = 0) uniform UBO {
 vec4 translation;
 vec4 rotation;
 vec4 global_scale;
 mat4 projection;
} camera;

//layout (binding = 1) buffer PrimitiveData {
// vec4 colours[];
//} primitive_data;

layout (location = 0) in vec3 vertex_position;

layout (location = 1) in vec3 instance_translation;
layout (location = 2) in vec3 instance_rotation;
layout (location = 3) in vec3 instance_scale;

mat4 translation_matrix(const vec3 v) {
	return mat4(
		1.0f, 0.0f, 0.0f, 0,
		0.0f, 1.0f, 0.0f, 0,
		0.0f, 0.0f, 1.0f, 0,
		v.x, v.y, v.z, 1.0f
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
 const vec4 object_transformation = 
  translation_matrix(instance_translation) * 
  quaternion_rotate_3d(
   scale_matrix(instance_scale) * vec4(vertex_position, 1.0), 
   instance_rotation
  );

// const vec4 camera_rotation = vec4(0, 2.9, 0, 1.0);
// const vec4 camera_translation = vec4(0, 0, -10, 1.0);

 gl_Position = 
  camera.projection * 
  quaternion_rotate_3d(
   translation_matrix(camera.translation.xyz) *
    scale_matrix(camera.global_scale.xyz) * 
    object_transformation,
   camera.rotation.xyz
  );
}