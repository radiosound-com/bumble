# Copyright 2021-2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: emulated_bluetooth_packets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n emulated_bluetooth_packets.proto\x12\x1b\x61ndroid.emulation.bluetooth\"\xfb\x01\n\tHCIPacket\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.android.emulation.bluetooth.HCIPacket.PacketType\x12\x0e\n\x06packet\x18\x02 \x01(\x0c\"\x9c\x01\n\nPacketType\x12\x1b\n\x17PACKET_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17PACKET_TYPE_HCI_COMMAND\x10\x01\x12\x13\n\x0fPACKET_TYPE_ACL\x10\x02\x12\x13\n\x0fPACKET_TYPE_SCO\x10\x03\x12\x15\n\x11PACKET_TYPE_EVENT\x10\x04\x12\x13\n\x0fPACKET_TYPE_ISO\x10\x05\x42J\n\x1f\x63om.android.emulation.bluetoothP\x01\xf8\x01\x01\xa2\x02\x03\x41\x45\x42\xaa\x02\x1b\x41ndroid.Emulation.Bluetoothb\x06proto3')



_HCIPACKET = DESCRIPTOR.message_types_by_name['HCIPacket']
_HCIPACKET_PACKETTYPE = _HCIPACKET.enum_types_by_name['PacketType']
HCIPacket = _reflection.GeneratedProtocolMessageType('HCIPacket', (_message.Message,), {
  'DESCRIPTOR' : _HCIPACKET,
  '__module__' : 'emulated_bluetooth_packets_pb2'
  # @@protoc_insertion_point(class_scope:android.emulation.bluetooth.HCIPacket)
  })
_sym_db.RegisterMessage(HCIPacket)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.android.emulation.bluetoothP\001\370\001\001\242\002\003AEB\252\002\033Android.Emulation.Bluetooth'
  _HCIPACKET._serialized_start=66
  _HCIPACKET._serialized_end=317
  _HCIPACKET_PACKETTYPE._serialized_start=161
  _HCIPACKET_PACKETTYPE._serialized_end=317
# @@protoc_insertion_point(module_scope)