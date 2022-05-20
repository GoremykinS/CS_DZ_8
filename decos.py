import sys
import traceback
import logging

# метод определения модуля, источника запуска
# Метод find() возвращает индекс первого вхождения искомой подстрочки
# если он найден в строке,
# если не найден, то возвращает 1

def log(func_to_log):
    # функции декораторы
    def log_saver(*args, **kwargs):
        logger_name = 'server' if 'server.py' in sys.argv[0] else 'client'
        LOGGER = logging.getLogger(logger_name)

        ret = func_to_log(*args, **kwargs)

        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} с параметрами {args}, {kwargs}.'
                     f'вызов из модуля {func_to_log.__module__}.'
                     f'вызов из функции {traceback.format_stack()[0].strip().split()[-1]}.'

        )

        return ret
    return log_saver





