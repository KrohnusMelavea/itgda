#version 430

layout (std430, binding = 1) buffer PrimitiveData {
 vec4 colours[];
} primitive_data;

uniform int colours_offset;

out vec4 fragment_colour;

void main() {
 fragment_colour = primitive_data.colours[colours_offset + gl_PrimitiveID];
 //fragment_colour = vec4(1.0f, 1.0f, 1.0f, 1.0f);
}