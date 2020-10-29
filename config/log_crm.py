import logging
import time

class Log_auto:



    def __init__(self):
        self.logger = logging.getLogger('log')
    def set_msg(self,mess,level_p):
        try:
            a = time.strftime('%Y-%m-%d', time.localtime())
            # 创建文件handle
            fh = logging.FileHandler('..\\..\\log_info\\wei_A_log' + a + '.log')
            # 创建控制台handle
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            # 对文件格式化

            fh.setFormatter(fm)
            # 对控制台格式化
            ch.setFormatter(fm)
            # 文件句柄加入
            self.logger.addHandler(fh)
            # 控制台句柄加入
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)
            # 输出info
            if level_p=='debug':
                self.logger.debug(mess)
            if level_p=='info':
                self.logger.info(mess)
            if level_p=='warning':
                self.logger.warning(mess)
            if level_p=='error':
                self.logger.error(mess)
            if level_p=='critical':
                self.logger.critical(mess)
            #移出文件句柄
            self.logger.removeHandler(fh)
            #移除控制台句柄
            self.logger.removeHandler(ch)
        except Exception as e:
            print(e)
        # 关闭文件
        finally:
            fh.close()

