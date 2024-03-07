# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_discovery/v1/service_registry.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+service_discovery/v1/service_registry.proto\x12\x10service_registry\"\x8d\x01\n\x0fServiceMetadata\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x0b\n\x03uri\x18\x04 \x01(\t\x12\x1a\n\x12\x63ommunication_kind\x18\x05 \x01(\t\x12\x1f\n\x17\x63ommunication_reference\x18\x06 \x01(\t\"E\n\x0fRegisterRequest\x12\x32\n\x07service\x18\x01 \x01(\x0b\x32!.service_registry.ServiceMetadata\"\x12\n\x10RegisterResponse\"E\n\x11UnregisterRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"\x14\n\x12UnregisterResponse\"C\n\x0f\x44iscoverRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"F\n\x10\x44iscoverResponse\x12\x32\n\x07service\x18\x01 \x01(\x0b\x32!.service_registry.ServiceMetadata\"/\n\x1a\x44iscoverByNamespaceRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\"R\n\x1b\x44iscoverByNamespaceResponse\x12\x33\n\x08services\x18\x01 \x03(\x0b\x32!.service_registry.ServiceMetadata\"\r\n\x0bListRequest\"C\n\x0cListResponse\x12\x33\n\x08services\x18\x01 \x03(\x0b\x32!.service_registry.ServiceMetadata2\xd5\x03\n\x0fServiceRegistry\x12S\n\x08Register\x12!.service_registry.RegisterRequest\x1a\".service_registry.RegisterResponse\"\x00\x12Y\n\nUnregister\x12#.service_registry.UnregisterRequest\x1a$.service_registry.UnregisterResponse\"\x00\x12S\n\x08\x44iscover\x12!.service_registry.DiscoverRequest\x1a\".service_registry.DiscoverResponse\"\x00\x12t\n\x13\x44iscoverByNamespace\x12,.service_registry.DiscoverByNamespaceRequest\x1a-.service_registry.DiscoverByNamespaceResponse\"\x00\x12G\n\x04List\x12\x1d.service_registry.ListRequest\x1a\x1e.service_registry.ListResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_discovery.v1.service_registry_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SERVICEMETADATA']._serialized_start=66
  _globals['_SERVICEMETADATA']._serialized_end=207
  _globals['_REGISTERREQUEST']._serialized_start=209
  _globals['_REGISTERREQUEST']._serialized_end=278
  _globals['_REGISTERRESPONSE']._serialized_start=280
  _globals['_REGISTERRESPONSE']._serialized_end=298
  _globals['_UNREGISTERREQUEST']._serialized_start=300
  _globals['_UNREGISTERREQUEST']._serialized_end=369
  _globals['_UNREGISTERRESPONSE']._serialized_start=371
  _globals['_UNREGISTERRESPONSE']._serialized_end=391
  _globals['_DISCOVERREQUEST']._serialized_start=393
  _globals['_DISCOVERREQUEST']._serialized_end=460
  _globals['_DISCOVERRESPONSE']._serialized_start=462
  _globals['_DISCOVERRESPONSE']._serialized_end=532
  _globals['_DISCOVERBYNAMESPACEREQUEST']._serialized_start=534
  _globals['_DISCOVERBYNAMESPACEREQUEST']._serialized_end=581
  _globals['_DISCOVERBYNAMESPACERESPONSE']._serialized_start=583
  _globals['_DISCOVERBYNAMESPACERESPONSE']._serialized_end=665
  _globals['_LISTREQUEST']._serialized_start=667
  _globals['_LISTREQUEST']._serialized_end=680
  _globals['_LISTRESPONSE']._serialized_start=682
  _globals['_LISTRESPONSE']._serialized_end=749
  _globals['_SERVICEREGISTRY']._serialized_start=752
  _globals['_SERVICEREGISTRY']._serialized_end=1221
# @@protoc_insertion_point(module_scope)
