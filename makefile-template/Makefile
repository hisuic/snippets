# Compiler to use
CC = gcc

# Compiler flags: 
#  -Wall enables common warnings
#  -Wextra enables additional warnings
#  -std=c11 enforces the C11 standard
CFLAGS = -Wall -Wextra -std=c11

# Linker flags (if any specific libraries are needed)
LDFLAGS = 

# Name of the output executable
TARGET = my_program

# Source files (.c files)
SRCS = main.c file1.c file2.c

# Object files (.o files, automatically generated from source files)
OBJS = $(SRCS:.c=.o)

# Default target: what runs when you just type `make`
# This will build the final executable by linking object files
all: $(TARGET)

# Rule to link object files into the final executable
# $@ represents the target, which is the executable name
# $^ represents all dependencies (object files in this case)
$(TARGET): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^

# Rule to compile each source file into an object file
# $< represents the first prerequisite (the source file in this case)
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean target: removes all object files and the executable
# Run this with `make clean`
clean:
	rm -f $(OBJS) $(TARGET)

# A useful phony target to ensure that `make` doesn't confuse the clean command with a file named 'clean'
.PHONY: all clean
