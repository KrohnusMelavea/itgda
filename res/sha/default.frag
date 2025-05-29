#version 420 core

in vec3 instance_fragment_colour;
out vec4 fragment_colour;

void main() {
 fragment_colour = vec4(instance_fragment_colour, 1.0f);
}