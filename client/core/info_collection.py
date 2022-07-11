import platform
import sys


class InfoCollection(object):

    def collect(self):
        # 收集平台信息
        try:
            func = getattr(self, platform.system().lower())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前操作系统：[%s]! " % platform.system())

    @staticmethod
    def linux():
        from plugins.collect_linux_info import collect
        return collect()

    @staticmethod
    def windows():
        from plugins.collect_windows_info from Win32Info
        return Win32Info().collect()

    @staticmethod
    def build_report_data(data):
        pass
        return data