#version 430

/* Question 5: Primitive-Based Colouring */
layout (std430, binding = 1) buffer PrimitiveData {
 vec4 colours[];
} primitive_data;

uniform int colours_offset; /* Question 5: Primitive-Based Colouring */

out vec4 fragment_colour;

void main() {
 fragment_colour = primitive_data.colours[colours_offset + gl_PrimitiveID]; /* Question 5: Primitive-Based Colouring */
}