U
    �.m^x  �                   @   s�  d dl Z d dlZd dlZe�d� ddddddd	d
ddddddgZdd� Zdd� Zdd� Zed� e	d�Z
e	d�Zed  dks�ed  dkr�dZndZe	d�Ze jed�Ze jed d!d"�Zz�e�r6zejjd#d$� W n   d%ZY nX e�d&� ejjd#ed'� ejjd#d(d)�d* d  d+ Zejjed d,� e�d(� nejjd-d(ed.� e�d&� W n   ed/� e�  Y nX ej�� d  d+ Zej jed0�d1 Z!ej jed0�d* Z e
d2k�r�e�  ne�  dS )3�    N�cleari)�	i���i��i��Qi ��i��Hi�*�
i��iLPi��_	i�:%i�i%oi���c            	      C   s:  d} t d� tj�� d }t|d �}t|d �D �] }tjj|d dd�d }t�d� |D ]�}|d d	 d
 }z|ztjj	|d� W n   d}Y nX tjj
|dd� tjj|dd�d d d
 }tjj|dd� t�d� tjj|d� W n   d}Y nX | d7 } t dtt| | d �� d � t�d� q^q2d S )Nr   z*[FSending messages...                    �count��   �   )�offsetr   �itemsZconversationZpeer�id��owner_idZpidor�	   Я гей��user_id�message�r   r   �Zmessage_idsZdelete_for_all�      �?z[FSending messages �d   �%   )�print�api�messagesZgetConversations�int�range�time�sleep�account�unban�send�
getHistory�deleteZban�str)	�quantityr   ZlapsZlapr   �itemr   �you�mg_id� r%   �troll.py�mgsp   s0    



 r'   c                  C   s�   d} t dd�}|�tj�� d d � tjjdd� td� t�d	� t	D ]V}|�t
|�d � tj	j|d
� | d	7 } tdt
t| t d �� d � t�d� qJt�d� |��  td� tD ]}tj	j|d
� t�d� q�tr�t�  td� d S )Nr   �backup�w�text�
r   �r*   z
[32mGroup's deletion...    r   �Zgroup_idz[FGroup's deletion r   r   r   皙�����?z%[FAdding the gay publics...         g      �?z![FDone:)                       
)�open�writer   �status�get�setr   r   r   �groupsr    �leaver   r   �close�pubs�join�mgr'   )r!   r)   �group�pubr%   r%   r&   �troll   s*    

 
r<   c                  C   s�   t dd�} tjj| �� d� td� t�d� tD ]}tjj	|d� t�d� q2td� d	}|r�| �� }|d t
|�d � }|d
kr�d}q\tjjt|�d� t�d� q\td� d S )Nr(   �rr,   z
[32mGay publics deletion...r   r-   r   z![FAdding the delited groups...  T� Fg�������?z*[FDone:(                                
)r/   r   r1   r3   �readliner   r   r   r4   r5   �lenr8   r   )r=   r:   Zreadingr;   r%   r%   r&   �untroll5   s"    

rA   uU  [37m
 InvertedOnes   @inverted_ones[32m
 ┏━━━━━┳━━━━━┳━━━━━┳━┓  ┏━┓
 ┗━┓ ┏━┫  ━  ┃  ┓  ┃ ┃  ┃ ┃
   ┃ ┃ ┃     ┫  ┗  ┃ ┗━━┫ ┗━━┓
   ┗━┛ ┗━━┻━━┻━━━━━┻━━━━┻━━━━┛

[35m[1] Troll
[2] Return
zSelect the option: [0mz![35mSend messages? [37my/n[0m �y�YTFz
[35mEnter the token: [0m)Zaccess_tokenz5.89Zru)�vZlangi�ϭr	   Zpidrr.   r   r   r   r   r   r   i
��)r
   Zpost_idr   z
[31mInvalid token
)r   r   �1)"Zvkr   �os�systemr7   r'   r<   rA   r   �inputZoptionr9   �tokenZSessionZsessionZAPIr   r   r   r#   r   r   r   r   r$   r   ZwallZcreateComment�quitZusersr2   r   r4   r   r%   r%   r%   r&   �<module>   sH   
 



