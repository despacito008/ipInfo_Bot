from get_ip import api_get_ip
from get_ip import get_ip_info

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! 发送 /help 获取命令信息", parse_mode='Markdown')

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="这是我刚才收到的信息: " + "*" +update.message.text +"*", parse_mode='Markdown')

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def help_info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/url *域名* 通过域名获取IP信息\n/ip *IP* 通过IP获取IP信息\n", parse_mode='Markdown')


def get_ip(update, context):
    print("Step 1：提取URL")
    url = ''.join(context.args)
    if len(url) == 0:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="您还未输入URL，请检查输入！",
            parse_mode='Markdown'
            )
    else:
        print(url)
        print("Step 2：调用api_get_ip函数")
        result = api_get_ip(url)
        print("回到Bot_Reply函数，查看返回的字典")
        print(result)
        status_str = result['status']
        print("查看状态码：" + status_str)
        print('Step 3：规则判断')
        if status_str == '1':
            ip = result['ip']
            print('调用ip-api函数，提取ip信息')
            ip_info = get_ip_info(ip)
            print('调用完毕，打印返回字典信息')
            print(ip_info)
            print('字典信息提取')
            status = ip_info['status']
            print('ip-api调用状态输出')
            print(status)
            if status == "fail":
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="域名IP查询失败，请检查域名是否正确！",
                    parse_mode='Markdown'
                )
            elif status == "success":
                country = ip_info['country']
                countryCode = ip_info['countryCode']
                isp = ip_info['isp']
                org = ip_info['org']
                ip_as = ip_info['as']
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="查询URL: " +"*" +url +"*" + "\n" + 
                        "解析IP: " +"*" +ip +"*" + "\n"+
                        "地理位置: " +"*" +country +"*" + "\n" +
                        "运营商: " +"*" +org +"*" + "\n"+
                        "ISP: " +"*" +isp +"*" + "\n"+
                        "AS: " +"*" +ip_as +"*",
                    parse_mode='Markdown'
                    )
            else:
                print('ip-api调用：失败')
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="API连接错误，请联系开发人员: [@Carrots_Fish_Bot](t.me/Carrots_Fish_Bot)",
                    parse_mode='Markdown'
                )
        elif status_str == '-4':
            print('状态判断：失败')
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="您输入的不是 *URL* 或 不支持此 *域名后缀*",
                parse_mode='Markdown'
            )
        else:
            print('状态判断：失败')
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="API连接错误，请联系开发人员: [@Carrots_Fish_Bot](t.me/Carrots_Fish_Bot)",
                parse_mode='Markdown'
            )

def input_ip(update, context):
    ip = ''.join(context.args)
    if len(ip) == 0:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="您还未输入IP，请检查输入！",
            parse_mode='Markdown'
            )
    else:
        print("取得用户输入IP: " + ip)
        ip_info = get_ip_info(ip)
        print('调用完毕，打印返回字典信息')
        print(ip_info)
        print('字典信息提取')
        status = ip_info['status']
        print('ip-api调用状态输出')
        if status == "success":
            country = ip_info['country']
            countryCode = ip_info['countryCode']
            isp = ip_info['isp']
            org = ip_info['org']
            ip_as = ip_info['as']
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="查询IP: " +"*" +ip +"*" + "\n" +
                    "地理位置: " +"*" +country +"*" + "\n" +
                    "运营商: " +"*" +org +"*" + "\n"+
                    "ISP: " +"*" +isp +"*" + "\n"+
                    "AS: " +"*" +ip_as +"*",
                parse_mode='Markdown'
                )
        elif status == "fail":
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="IP信息查询失败，请检查IP是否正确！",
                parse_mode='Markdown'
                )
        else:
            print('ip-api调用：失败')
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="API连接错误，请联系开发人员: [@Carrots_Fish_Bot](t.me/Carrots_Fish_Bot)",
                parse_mode='Markdown'
                )