#version 420 core

layout (binding = 0) readonly buffer PrimitiveData {
    vec3 colours[];
} primitive_data;

out vec4 fragment_colour;

void main() {
 fragment_colour = vec4(primitive_data.colours[gl_PrimitiveId], 1.0f);
}