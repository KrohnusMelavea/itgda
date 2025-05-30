#version 430 core

layout (binding = 3) readonly buffer PrimitiveData {
    vec3 colours[];
} primitive_data;

out vec4 fragment_colour;

void main() {
 fragment_colour = vec4(primitive_data.colours[0], 1.0f);
 //fragment_colour = vec4(1.0f, 1.0f, 1.0f, 1.0f);
}