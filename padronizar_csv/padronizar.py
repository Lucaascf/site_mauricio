#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para padronizar arquivos CSV
Converte todos os CSVs para usar vírgula como delimitador padrão
Remove aspas desnecessárias e normaliza a codificação
"""

import csv
import os
import shutil
from pathlib import Path
import chardet

def detect_encoding(file_path):
    """Detecta a codificação do arquivo"""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def detect_delimiter(file_path, encoding='utf-8'):
    """Detecta o delimitador usado no CSV"""
    try:
        with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
            # Lê as primeiras linhas para detectar o delimitador
            first_lines = []
            for i, line in enumerate(f):
                if i >= 5:  # Analisa apenas as primeiras 5 linhas
                    break
                first_lines.append(line)
            
            # Testa diferentes delimitadores
            delimiters = [';', ',', '\t', '|']
            delimiter_scores = {}
            
            for delimiter in delimiters:
                scores = []
                for line in first_lines:
                    if line.strip():  # Ignora linhas vazias
                        count = line.count(delimiter)
                        scores.append(count)
                
                if scores:
                    # Verifica consistência (mesmo número de delimitadores por linha)
                    avg_score = sum(scores) / len(scores)
                    consistency = 1 - (max(scores) - min(scores)) / (max(scores) + 1)
                    delimiter_scores[delimiter] = avg_score * consistency
            
            # Retorna o delimitador com maior pontuação
            if delimiter_scores:
                best_delimiter = max(delimiter_scores, key=delimiter_scores.get)
                return best_delimiter if delimiter_scores[best_delimiter] > 0 else ';'
            
            return ';'  # Padrão se não conseguir detectar
            
    except Exception as e:
        print(f"Erro ao detectar delimitador em {file_path}: {e}")
        return ';'

def clean_field(field):
    """Remove aspas desnecessárias e limpa o campo"""
    if field is None:
        return ''
    
    field = str(field).strip()
    
    # Remove aspas duplas no início e fim se estiverem presentes
    if field.startswith('"') and field.endswith('"'):
        field = field[1:-1]
    
    # Remove aspas duplas extras internas
    field = field.replace('""', '"')
    
    return field

def standardize_csv(input_file, output_file=None, target_delimiter=',', target_encoding='utf-8'):
    """
    Padroniza um arquivo CSV
    
    Args:
        input_file: Caminho do arquivo de entrada
        output_file: Caminho do arquivo de saída (se None, substitui o original)
        target_delimiter: Delimitador desejado (padrão: vírgula)
        target_encoding: Codificação desejada (padrão: utf-8)
    """
    
    if output_file is None:
        output_file = input_file
    
    try:
        # Detecta a codificação atual
        current_encoding = detect_encoding(input_file)
        print(f"Processando {os.path.basename(input_file)}...")
        print(f"  Codificação detectada: {current_encoding}")
        
        # Detecta o delimitador atual
        current_delimiter = detect_delimiter(input_file, current_encoding)
        print(f"  Delimitador detectado: '{current_delimiter}'")
        
        # Lê o arquivo original
        rows = []
        with open(input_file, 'r', encoding=current_encoding, errors='ignore') as f:
            # Usa csv.Sniffer para detectar automaticamente o formato
            try:
                sample = f.read(1024)
                f.seek(0)
                sniffer = csv.Sniffer()
                
                # Tenta detectar automaticamente
                try:
                    dialect = sniffer.sniff(sample, delimiters=';,\t|')
                    reader = csv.reader(f, dialect)
                except:
                    # Se falhar, usa o delimitador detectado manualmente
                    reader = csv.reader(f, delimiter=current_delimiter, quotechar='"')
                
                for row in reader:
                    # Limpa cada campo da linha
                    cleaned_row = [clean_field(field) for field in row]
                    rows.append(cleaned_row)
                    
            except Exception as e:
                print(f"  Erro ao processar com csv.reader: {e}")
                # Fallback: processa linha por linha manualmente
                f.seek(0)
                for line in f:
                    line = line.strip()
                    if line:
                        # Split manual usando o delimitador detectado
                        fields = line.split(current_delimiter)
                        cleaned_row = [clean_field(field) for field in fields]
                        rows.append(cleaned_row)
        
        # Escreve o arquivo padronizado
        with open(output_file, 'w', encoding=target_encoding, newline='') as f:
            writer = csv.writer(f, delimiter=target_delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(rows)
        
        print(f"  ✓ Arquivo padronizado salvo: {os.path.basename(output_file)}")
        print(f"  ✓ Linhas processadas: {len(rows)}")
        print(f"  ✓ Delimitador final: '{target_delimiter}'")
        print(f"  ✓ Codificação final: {target_encoding}")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Erro ao processar {input_file}: {e}")
        return False

def quick_standardize():
    """Versão simplificada - padroniza todos os CSVs para vírgula"""
    
    # PASTAS DE TRABALHO
    source_folder = "/home/lusca/Downloads/lucas2csvs"
    output_folder = "/home/lusca/Downloads/lucas2csvs_padronizados"
    
    # Lista dos seus arquivos CSV
    csv_files = [
        'produto.csv',
        'Pedido.csv', 
        'ocorpedf.csv',
        'ocorpedc.csv',
        'ocorfor.csv',
        'ocorcot.csv',
        'ocorcli.csv',
        'forneced.csv',
        'cotacao.csv',
        'cliente.csv'
    ]
    
    print("=== PADRONIZAÇÃO RÁPIDA ===")
    print(f"Pasta origem: {source_folder}")
    print(f"Pasta destino: {output_folder}")
    print("Convertendo todos os CSVs para usar vírgula como delimitador...")
    print()
    
    # Verifica se a pasta origem existe
    if not os.path.exists(source_folder):
        print(f"❌ ERRO: Pasta origem não encontrada: {source_folder}")
        print("Verifique se o caminho está correto!")
        return
    
    # Cria a pasta de destino se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"✓ Pasta de destino criada: {output_folder}")
    
    processed_count = 0
    for filename in csv_files:
        source_file = os.path.join(source_folder, filename)
        output_file = os.path.join(output_folder, filename)
        
        if os.path.exists(source_file):
            if standardize_csv(source_file, output_file, target_delimiter=','):
                print(f"✓ {filename} padronizado e salvo!")
                processed_count += 1
            else:
                print(f"✗ Erro ao processar {filename}")
        else:
            print(f"⚠️  Arquivo não encontrado: {filename}")
        print("-" * 30)
    
    print(f"\n🎉 Padronização concluída!")
    print(f"Arquivos processados: {processed_count}/{len(csv_files)}")
    print(f"Arquivos originais mantidos em: {source_folder}")
    print(f"Arquivos padronizados salvos em: {output_folder}")

def main():
    """Função principal"""
    print("=== PADRONIZADOR DE ARQUIVOS CSV ===")
    print("Pasta origem: /home/lusca/Downloads/lucas2csvs")
    print("Pasta destino: /home/lusca/Downloads/lucas2csvs_padronizados")
    print("Delimitador padrão: vírgula (,)")
    print("Codificação padrão: UTF-8")
    print()
    
    # Pastas
    source_folder = "/home/lusca/Downloads/lucas2csvs"
    output_folder = "/home/lusca/Downloads/lucas2csvs_padronizados"
    
    # Verifica se a pasta origem existe
    if not os.path.exists(source_folder):
        print(f"❌ ERRO: Pasta origem não encontrada: {source_folder}")
        print("Verifique se o caminho está correto!")
        return
    
    # Pergunta se o usuário quer continuar
    response = input("Deseja continuar? (s/n): ").lower().strip()
    if response not in ['s', 'sim', 'y', 'yes']:
        print("Operação cancelada.")
        return
    
    # Opção de escolher delimitador
    print("\nEscolha o delimitador alvo:")
    print("1. Vírgula (,) - Recomendado")
    print("2. Ponto-e-vírgula (;)")
    print("3. Tab (\\t)")
    
    choice = input("Digite sua escolha (1-3) ou pressione Enter para vírgula: ").strip()
    
    delimiter_map = {
        '1': ',',
        '2': ';',
        '3': '\t',
        '': ','
    }
    
    target_delimiter = delimiter_map.get(choice, ',')
    
    print(f"\nDelimitador escolhido: '{target_delimiter}'")
    print("Iniciando processamento...\n")
    
    # Cria a pasta de destino se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"✓ Pasta de destino criada: {output_folder}")
    
    # Processa todos os CSVs da pasta origem
    csv_files = list(Path(source_folder).glob('*.csv'))
    
    if not csv_files:
        print(f"Nenhum arquivo CSV encontrado em: {source_folder}")
        return
    
    print(f"Encontrados {len(csv_files)} arquivos CSV:")
    for file in csv_files:
        print(f"  - {file.name}")
    
    print(f"\nIniciando padronização...")
    print(f"Delimitador alvo: '{target_delimiter}'")
    print("-" * 50)
    
    success_count = 0
    for csv_file in csv_files:
        source_file = str(csv_file)
        output_file = os.path.join(output_folder, csv_file.name)
        
        if standardize_csv(source_file, output_file, target_delimiter=target_delimiter):
            success_count += 1
        print("-" * 30)
    
    print(f"\nResultado:")
    print(f"✓ Arquivos processados com sucesso: {success_count}/{len(csv_files)}")
    print(f"Arquivos originais mantidos em: {source_folder}")
    print(f"Arquivos padronizados salvos em: {output_folder}")
    
    if success_count == len(csv_files):
        print("🎉 Todos os arquivos foram padronizados com sucesso!")
    else:
        print("⚠️  Alguns arquivos apresentaram problemas. Verifique os logs acima.")

if __name__ == "__main__":
    main()

# ========================================
# EXECUÇÃO AUTOMÁTICA - DESCOMENTE A LINHA ABAIXO
# ========================================
# quick_standardize()