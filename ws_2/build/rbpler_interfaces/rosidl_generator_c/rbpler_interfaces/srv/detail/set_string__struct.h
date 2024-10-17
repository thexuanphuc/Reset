// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from rbpler_interfaces:srv/SetString.idl
// generated code does not contain a copyright notice

#ifndef RBPLER_INTERFACES__SRV__DETAIL__SET_STRING__STRUCT_H_
#define RBPLER_INTERFACES__SRV__DETAIL__SET_STRING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SetString in the package rbpler_interfaces.
typedef struct rbpler_interfaces__srv__SetString_Request
{
  rosidl_runtime_c__String data;
} rbpler_interfaces__srv__SetString_Request;

// Struct for a sequence of rbpler_interfaces__srv__SetString_Request.
typedef struct rbpler_interfaces__srv__SetString_Request__Sequence
{
  rbpler_interfaces__srv__SetString_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rbpler_interfaces__srv__SetString_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SetString in the package rbpler_interfaces.
typedef struct rbpler_interfaces__srv__SetString_Response
{
  bool success;
  rosidl_runtime_c__String message;
} rbpler_interfaces__srv__SetString_Response;

// Struct for a sequence of rbpler_interfaces__srv__SetString_Response.
typedef struct rbpler_interfaces__srv__SetString_Response__Sequence
{
  rbpler_interfaces__srv__SetString_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rbpler_interfaces__srv__SetString_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // RBPLER_INTERFACES__SRV__DETAIL__SET_STRING__STRUCT_H_
