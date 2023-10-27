# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bos/v1/performance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from ...bos.v1 import common_pb2 as bos_dot_v1_dot_common__pb2
from ...bos.v1 import constraints_pb2 as bos_dot_v1_dot_constraints__pb2
from ...bos.v1 import units_pb2 as bos_dot_v1_dot_units__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18\x62os/v1/performance.proto\x12\x0e\x62raiins.bos.v1\x1a\x13\x62os/v1/common.proto\x1a\x18\x62os/v1/constraints.proto\x1a\x12\x62os/v1/units.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdd\x01\n\x12TunerConfiguration\x12\x14\n\x07\x65nabled\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x32\n\ntuner_mode\x18\x02 \x01(\x0e\x32\x19.braiins.bos.v1.TunerModeH\x01\x88\x01\x01\x12+\n\x0cpower_target\x18\x03 \x01(\x0b\x32\x15.braiins.bos.v1.Power\x12\x35\n\x0fhashrate_target\x18\x04 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrateB\n\n\x08_enabledB\r\n\x0b_tuner_mode"\x88\x01\n\x10TunerConstraints\x12\x36\n\x0cpower_target\x18\x01 \x01(\x0b\x32 .braiins.bos.v1.PowerConstraints\x12<\n\x0fhashrate_target\x18\x02 \x01(\x0b\x32#.braiins.bos.v1.HashrateConstraints"\xe6\x02\n\x10\x44PSConfiguration\x12\x14\n\x07\x65nabled\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12)\n\npower_step\x18\x02 \x01(\x0b\x32\x15.braiins.bos.v1.Power\x12\x33\n\rhashrate_step\x18\x03 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate\x12/\n\x10min_power_target\x18\x04 \x01(\x0b\x32\x15.braiins.bos.v1.Power\x12\x39\n\x13min_hashrate_target\x18\x05 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate\x12\x1d\n\x10shutdown_enabled\x18\x06 \x01(\x08H\x01\x88\x01\x01\x12\x30\n\x11shutdown_duration\x18\x07 \x01(\x0b\x32\x15.braiins.bos.v1.HoursB\n\n\x08_enabledB\x13\n\x11_shutdown_enabled"\xbe\x01\n!HashboardPerformanceConfiguration\x12\x33\n\x10global_frequency\x18\x01 \x01(\x0b\x32\x19.braiins.bos.v1.Frequency\x12/\n\x0eglobal_voltage\x18\x02 \x01(\x0b\x32\x17.braiins.bos.v1.Voltage\x12\x33\n\nhashboards\x18\x03 \x03(\x0b\x32\x1f.braiins.bos.v1.HashboardConfig"\xfd\x02\n\x0e\x44PSConstraints\x12\x34\n\npower_step\x18\x01 \x01(\x0b\x32 .braiins.bos.v1.PowerConstraints\x12:\n\rhashrate_step\x18\x02 \x01(\x0b\x32#.braiins.bos.v1.HashrateConstraints\x12:\n\x10min_power_target\x18\x03 \x01(\x0b\x32 .braiins.bos.v1.PowerConstraints\x12@\n\x13min_hashrate_target\x18\x04 \x01(\x0b\x32#.braiins.bos.v1.HashrateConstraints\x12;\n\x10shutdown_enabled\x18\x05 \x01(\x0b\x32!.braiins.bos.v1.BooleanConstraint\x12>\n\x11shutdown_duration\x18\x06 \x01(\x0b\x32#.braiins.bos.v1.DurationConstraints"\xcf\x01\n\x14HashboardConstraints\x12\x15\n\rhashboard_ids\x18\x01 \x03(\t\x12\x32\n\x07\x65nabled\x18\x02 \x01(\x0b\x32!.braiins.bos.v1.BooleanConstraint\x12\x37\n\tfrequency\x18\x03 \x01(\x0b\x32$.braiins.bos.v1.FrequencyConstraints\x12\x33\n\x07voltage\x18\x04 \x01(\x0b\x32".braiins.bos.v1.VoltageConstraints"\xdd\x01\n\x12PowerTargetProfile\x12+\n\x07\x63reated\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x06target\x18\x02 \x01(\x0b\x32\x15.braiins.bos.v1.Power\x12\x37\n\x11measured_hashrate\x18\x03 \x01(\x0b\x32\x1c.braiins.bos.v1.GigaHashrate\x12:\n\x1b\x65stimated_power_consumption\x18\x04 \x01(\x0b\x32\x15.braiins.bos.v1.Power"\xe7\x01\n\x15HashrateTargetProfile\x12+\n\x07\x63reated\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x06target\x18\x02 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate\x12\x37\n\x11measured_hashrate\x18\x03 \x01(\x0b\x32\x1c.braiins.bos.v1.GigaHashrate\x12:\n\x1b\x65stimated_power_consumption\x18\x04 \x01(\x0b\x32\x15.braiins.bos.v1.Power"\x16\n\x14GetTunerStateRequest"\xf6\x01\n\x15GetTunerStateResponse\x12\x37\n\x13overall_tuner_state\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.TunerState\x12G\n\x17power_target_mode_state\x18\x02 \x01(\x0b\x32$.braiins.bos.v1.PowerTargetModeStateH\x00\x12M\n\x1ahashrate_target_mode_state\x18\x03 \x01(\x0b\x32\'.braiins.bos.v1.HashrateTargetModeStateH\x00\x42\x0c\n\nmode_state"z\n\x14PowerTargetModeState\x12\x33\n\x07profile\x18\x01 \x01(\x0b\x32".braiins.bos.v1.PowerTargetProfile\x12-\n\x0e\x63urrent_target\x18\x02 \x01(\x0b\x32\x15.braiins.bos.v1.Power"\x87\x01\n\x17HashrateTargetModeState\x12\x36\n\x07profile\x18\x01 \x01(\x0b\x32%.braiins.bos.v1.HashrateTargetProfile\x12\x34\n\x0e\x63urrent_target\x18\x02 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate"\x1b\n\x19ListTargetProfilesRequest"\xa8\x01\n\x1aListTargetProfilesResponse\x12\x41\n\x15power_target_profiles\x18\x01 \x03(\x0b\x32".braiins.bos.v1.PowerTargetProfile\x12G\n\x18hashrate_target_profiles\x18\x02 \x03(\x0b\x32%.braiins.bos.v1.HashrateTargetProfile"O\n\x1cSetDefaultPowerTargetRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction"u\n\x15SetPowerTargetRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12+\n\x0cpower_target\x18\x02 \x01(\x0b\x32\x15.braiins.bos.v1.Power"\x85\x01\n\x1bIncrementPowerTargetRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12\x35\n\x16power_target_increment\x18\x02 \x01(\x0b\x32\x15.braiins.bos.v1.Power"\x85\x01\n\x1b\x44\x65\x63rementPowerTargetRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12\x35\n\x16power_target_decrement\x18\x02 \x01(\x0b\x32\x15.braiins.bos.v1.Power"E\n\x16SetPowerTargetResponse\x12+\n\x0cpower_target\x18\x01 \x01(\x0b\x32\x15.braiins.bos.v1.Power"R\n\x1fSetDefaultHashrateTargetRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction"\x82\x01\n\x18SetHashrateTargetRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12\x35\n\x0fhashrate_target\x18\x02 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate"\x92\x01\n\x1eIncrementHashrateTargetRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12?\n\x19hashrate_target_increment\x18\x02 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate"\x92\x01\n\x1e\x44\x65\x63rementHashrateTargetRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12?\n\x19hashrate_target_decrement\x18\x02 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate"R\n\x19SetHashrateTargetResponse\x12\x35\n\x0fhashrate_target\x18\x01 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate"l\n\x0e\x44PSPowerTarget\x12)\n\npower_step\x18\x01 \x01(\x0b\x32\x15.braiins.bos.v1.Power\x12/\n\x10min_power_target\x18\x02 \x01(\x0b\x32\x15.braiins.bos.v1.Power"\x83\x01\n\x11\x44PSHashrateTarget\x12\x33\n\rhashrate_step\x18\x01 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate\x12\x39\n\x13min_hashrate_target\x18\x02 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate"\x8b\x01\n\tDPSTarget\x12\x36\n\x0cpower_target\x18\x01 \x01(\x0b\x32\x1e.braiins.bos.v1.DPSPowerTargetH\x00\x12<\n\x0fhashrate_target\x18\x02 \x01(\x0b\x32!.braiins.bos.v1.DPSHashrateTargetH\x00\x42\x08\n\x06target"\x8a\x02\n\rSetDPSRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12\x13\n\x06\x65nable\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x1c\n\x0f\x65nable_shutdown\x18\x03 \x01(\x08H\x01\x88\x01\x01\x12\x35\n\x11shutdown_duration\x18\x04 \x01(\x0b\x32\x15.braiins.bos.v1.HoursH\x02\x88\x01\x01\x12)\n\x06target\x18\x05 \x01(\x0b\x32\x19.braiins.bos.v1.DPSTargetB\t\n\x07_enableB\x12\n\x10_enable_shutdownB\x14\n\x12_shutdown_duration"\xa5\x02\n\x0eSetDPSResponse\x12\x14\n\x07\x65nabled\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x1d\n\x10shutdown_enabled\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x35\n\x11shutdown_duration\x18\x03 \x01(\x0b\x32\x15.braiins.bos.v1.HoursH\x02\x88\x01\x01\x12\x34\n\x0cpower_target\x18\x04 \x01(\x0b\x32\x1e.braiins.bos.v1.DPSPowerTarget\x12:\n\x0fhashrate_target\x18\x05 \x01(\x0b\x32!.braiins.bos.v1.DPSHashrateTargetB\n\n\x08_enabledB\x13\n\x11_shutdown_enabledB\x14\n\x12_shutdown_duration"\x82\x01\n\x1cHashboardPerformanceSettings\x12\n\n\x02id\x18\x01 \x01(\t\x12,\n\tfrequency\x18\x02 \x01(\x0b\x32\x19.braiins.bos.v1.Frequency\x12(\n\x07voltage\x18\x03 \x01(\x0b\x32\x17.braiins.bos.v1.Voltage"\x97\x01\n\x0fHashboardConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x07\x65nabled\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12,\n\tfrequency\x18\x03 \x01(\x0b\x32\x19.braiins.bos.v1.Frequency\x12(\n\x07voltage\x18\x04 \x01(\x0b\x32\x17.braiins.bos.v1.VoltageB\n\n\x08_enabled"\xbf\x01\n\x15ManualPerformanceMode\x12\x33\n\x10global_frequency\x18\x01 \x01(\x0b\x32\x19.braiins.bos.v1.Frequency\x12/\n\x0eglobal_voltage\x18\x02 \x01(\x0b\x32\x17.braiins.bos.v1.Voltage\x12@\n\nhashboards\x18\x03 \x03(\x0b\x32,.braiins.bos.v1.HashboardPerformanceSettings">\n\x0fPowerTargetMode\x12+\n\x0cpower_target\x18\x01 \x01(\x0b\x32\x15.braiins.bos.v1.Power"K\n\x12HashrateTargetMode\x12\x35\n\x0fhashrate_target\x18\x01 \x01(\x0b\x32\x1c.braiins.bos.v1.TeraHashrate"\x98\x01\n\x14TunerPerformanceMode\x12\x37\n\x0cpower_target\x18\x01 \x01(\x0b\x32\x1f.braiins.bos.v1.PowerTargetModeH\x00\x12=\n\x0fhashrate_target\x18\x02 \x01(\x0b\x32".braiins.bos.v1.HashrateTargetModeH\x00\x42\x08\n\x06target"{\n\x19SetPerformanceModeRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12-\n\x04mode\x18\x02 \x01(\x0b\x32\x1f.braiins.bos.v1.PerformanceMode"\x93\x01\n\x0fPerformanceMode\x12<\n\x0bmanual_mode\x18\x01 \x01(\x0b\x32%.braiins.bos.v1.ManualPerformanceModeH\x00\x12:\n\ntuner_mode\x18\x02 \x01(\x0b\x32$.braiins.bos.v1.TunerPerformanceModeH\x00\x42\x06\n\x04mode"\x1b\n\x19GetPerformanceModeRequest*d\n\tTunerMode\x12\x1a\n\x16TUNER_MODE_UNSPECIFIED\x10\x00\x12\x1b\n\x17TUNER_MODE_POWER_TARGET\x10\x01\x12\x1e\n\x1aTUNER_MODE_HASHRATE_TARGET\x10\x02*\x8a\x01\n\nTunerState\x12\x1b\n\x17TUNER_STATE_UNSPECIFIED\x10\x00\x12\x18\n\x14TUNER_STATE_DISABLED\x10\x01\x12\x16\n\x12TUNER_STATE_STABLE\x10\x02\x12\x16\n\x12TUNER_STATE_TUNING\x10\x03\x12\x15\n\x11TUNER_STATE_ERROR\x10\x04\x32\xea\n\n\x12PerformanceService\x12\\\n\rGetTunerState\x12$.braiins.bos.v1.GetTunerStateRequest\x1a%.braiins.bos.v1.GetTunerStateResponse\x12k\n\x12ListTargetProfiles\x12).braiins.bos.v1.ListTargetProfilesRequest\x1a*.braiins.bos.v1.ListTargetProfilesResponse\x12m\n\x15SetDefaultPowerTarget\x12,.braiins.bos.v1.SetDefaultPowerTargetRequest\x1a&.braiins.bos.v1.SetPowerTargetResponse\x12_\n\x0eSetPowerTarget\x12%.braiins.bos.v1.SetPowerTargetRequest\x1a&.braiins.bos.v1.SetPowerTargetResponse\x12k\n\x14IncrementPowerTarget\x12+.braiins.bos.v1.IncrementPowerTargetRequest\x1a&.braiins.bos.v1.SetPowerTargetResponse\x12k\n\x14\x44\x65\x63rementPowerTarget\x12+.braiins.bos.v1.DecrementPowerTargetRequest\x1a&.braiins.bos.v1.SetPowerTargetResponse\x12v\n\x18SetDefaultHashrateTarget\x12/.braiins.bos.v1.SetDefaultHashrateTargetRequest\x1a).braiins.bos.v1.SetHashrateTargetResponse\x12h\n\x11SetHashrateTarget\x12(.braiins.bos.v1.SetHashrateTargetRequest\x1a).braiins.bos.v1.SetHashrateTargetResponse\x12t\n\x17IncrementHashrateTarget\x12..braiins.bos.v1.IncrementHashrateTargetRequest\x1a).braiins.bos.v1.SetHashrateTargetResponse\x12t\n\x17\x44\x65\x63rementHashrateTarget\x12..braiins.bos.v1.DecrementHashrateTargetRequest\x1a).braiins.bos.v1.SetHashrateTargetResponse\x12G\n\x06SetDPS\x12\x1d.braiins.bos.v1.SetDPSRequest\x1a\x1e.braiins.bos.v1.SetDPSResponse\x12`\n\x12SetPerformanceMode\x12).braiins.bos.v1.SetPerformanceModeRequest\x1a\x1f.braiins.bos.v1.PerformanceMode\x12\x66\n\x18GetActivePerformanceMode\x12).braiins.bos.v1.GetPerformanceModeRequest\x1a\x1f.braiins.bos.v1.PerformanceModeb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "bos.v1.performance_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_TUNERMODE"]._serialized_start = 6022
    _globals["_TUNERMODE"]._serialized_end = 6122
    _globals["_TUNERSTATE"]._serialized_start = 6125
    _globals["_TUNERSTATE"]._serialized_end = 6263
    _globals["_TUNERCONFIGURATION"]._serialized_start = 145
    _globals["_TUNERCONFIGURATION"]._serialized_end = 366
    _globals["_TUNERCONSTRAINTS"]._serialized_start = 369
    _globals["_TUNERCONSTRAINTS"]._serialized_end = 505
    _globals["_DPSCONFIGURATION"]._serialized_start = 508
    _globals["_DPSCONFIGURATION"]._serialized_end = 866
    _globals["_HASHBOARDPERFORMANCECONFIGURATION"]._serialized_start = 869
    _globals["_HASHBOARDPERFORMANCECONFIGURATION"]._serialized_end = 1059
    _globals["_DPSCONSTRAINTS"]._serialized_start = 1062
    _globals["_DPSCONSTRAINTS"]._serialized_end = 1443
    _globals["_HASHBOARDCONSTRAINTS"]._serialized_start = 1446
    _globals["_HASHBOARDCONSTRAINTS"]._serialized_end = 1653
    _globals["_POWERTARGETPROFILE"]._serialized_start = 1656
    _globals["_POWERTARGETPROFILE"]._serialized_end = 1877
    _globals["_HASHRATETARGETPROFILE"]._serialized_start = 1880
    _globals["_HASHRATETARGETPROFILE"]._serialized_end = 2111
    _globals["_GETTUNERSTATEREQUEST"]._serialized_start = 2113
    _globals["_GETTUNERSTATEREQUEST"]._serialized_end = 2135
    _globals["_GETTUNERSTATERESPONSE"]._serialized_start = 2138
    _globals["_GETTUNERSTATERESPONSE"]._serialized_end = 2384
    _globals["_POWERTARGETMODESTATE"]._serialized_start = 2386
    _globals["_POWERTARGETMODESTATE"]._serialized_end = 2508
    _globals["_HASHRATETARGETMODESTATE"]._serialized_start = 2511
    _globals["_HASHRATETARGETMODESTATE"]._serialized_end = 2646
    _globals["_LISTTARGETPROFILESREQUEST"]._serialized_start = 2648
    _globals["_LISTTARGETPROFILESREQUEST"]._serialized_end = 2675
    _globals["_LISTTARGETPROFILESRESPONSE"]._serialized_start = 2678
    _globals["_LISTTARGETPROFILESRESPONSE"]._serialized_end = 2846
    _globals["_SETDEFAULTPOWERTARGETREQUEST"]._serialized_start = 2848
    _globals["_SETDEFAULTPOWERTARGETREQUEST"]._serialized_end = 2927
    _globals["_SETPOWERTARGETREQUEST"]._serialized_start = 2929
    _globals["_SETPOWERTARGETREQUEST"]._serialized_end = 3046
    _globals["_INCREMENTPOWERTARGETREQUEST"]._serialized_start = 3049
    _globals["_INCREMENTPOWERTARGETREQUEST"]._serialized_end = 3182
    _globals["_DECREMENTPOWERTARGETREQUEST"]._serialized_start = 3185
    _globals["_DECREMENTPOWERTARGETREQUEST"]._serialized_end = 3318
    _globals["_SETPOWERTARGETRESPONSE"]._serialized_start = 3320
    _globals["_SETPOWERTARGETRESPONSE"]._serialized_end = 3389
    _globals["_SETDEFAULTHASHRATETARGETREQUEST"]._serialized_start = 3391
    _globals["_SETDEFAULTHASHRATETARGETREQUEST"]._serialized_end = 3473
    _globals["_SETHASHRATETARGETREQUEST"]._serialized_start = 3476
    _globals["_SETHASHRATETARGETREQUEST"]._serialized_end = 3606
    _globals["_INCREMENTHASHRATETARGETREQUEST"]._serialized_start = 3609
    _globals["_INCREMENTHASHRATETARGETREQUEST"]._serialized_end = 3755
    _globals["_DECREMENTHASHRATETARGETREQUEST"]._serialized_start = 3758
    _globals["_DECREMENTHASHRATETARGETREQUEST"]._serialized_end = 3904
    _globals["_SETHASHRATETARGETRESPONSE"]._serialized_start = 3906
    _globals["_SETHASHRATETARGETRESPONSE"]._serialized_end = 3988
    _globals["_DPSPOWERTARGET"]._serialized_start = 3990
    _globals["_DPSPOWERTARGET"]._serialized_end = 4098
    _globals["_DPSHASHRATETARGET"]._serialized_start = 4101
    _globals["_DPSHASHRATETARGET"]._serialized_end = 4232
    _globals["_DPSTARGET"]._serialized_start = 4235
    _globals["_DPSTARGET"]._serialized_end = 4374
    _globals["_SETDPSREQUEST"]._serialized_start = 4377
    _globals["_SETDPSREQUEST"]._serialized_end = 4643
    _globals["_SETDPSRESPONSE"]._serialized_start = 4646
    _globals["_SETDPSRESPONSE"]._serialized_end = 4939
    _globals["_HASHBOARDPERFORMANCESETTINGS"]._serialized_start = 4942
    _globals["_HASHBOARDPERFORMANCESETTINGS"]._serialized_end = 5072
    _globals["_HASHBOARDCONFIG"]._serialized_start = 5075
    _globals["_HASHBOARDCONFIG"]._serialized_end = 5226
    _globals["_MANUALPERFORMANCEMODE"]._serialized_start = 5229
    _globals["_MANUALPERFORMANCEMODE"]._serialized_end = 5420
    _globals["_POWERTARGETMODE"]._serialized_start = 5422
    _globals["_POWERTARGETMODE"]._serialized_end = 5484
    _globals["_HASHRATETARGETMODE"]._serialized_start = 5486
    _globals["_HASHRATETARGETMODE"]._serialized_end = 5561
    _globals["_TUNERPERFORMANCEMODE"]._serialized_start = 5564
    _globals["_TUNERPERFORMANCEMODE"]._serialized_end = 5716
    _globals["_SETPERFORMANCEMODEREQUEST"]._serialized_start = 5718
    _globals["_SETPERFORMANCEMODEREQUEST"]._serialized_end = 5841
    _globals["_PERFORMANCEMODE"]._serialized_start = 5844
    _globals["_PERFORMANCEMODE"]._serialized_end = 5991
    _globals["_GETPERFORMANCEMODEREQUEST"]._serialized_start = 5993
    _globals["_GETPERFORMANCEMODEREQUEST"]._serialized_end = 6020
    _globals["_PERFORMANCESERVICE"]._serialized_start = 6266
    _globals["_PERFORMANCESERVICE"]._serialized_end = 7652
# @@protoc_insertion_point(module_scope)
