import yaml

def create_compose_config(node_ids):
    """生成包含多个nexus-cli服务的docker-compose配置"""
    config = {
        'version': '3.8',
        'services': {
            f'nexus-cli-{node_id}': {
                'image': 'nexus-cli',
                'command': ['start', '--headless', f'--node-id={node_id}'],                             
                'restart': 'unless-stopped'
            } for node_id in node_ids
        }
    }
    return yaml.dump(config, sort_keys=False, width=1000)

if __name__ == '__main__':
    # 示例节点ID数组
    sample_ids =   [111,112]
    with open('docker-compose.yml', 'w') as f:
        f.write(create_compose_config(sample_ids))
    print("docker-compose.yml 文件已生成")
